/* Service worker for the Might & Magic card browser.
 *
 * Staleness is the enemy here: card data changes often, so the only thing
 * cached ahead of a network attempt is art, which never changes once added.
 * Everything else is network-first and falls back to cache only when offline.
 *
 * VERSION is bumped on every deploy by bump-version.mjs, which also updates
 * the badge in index.html. It names the cache, so activating a new worker
 * drops every byte the previous release cached.
 */
const VERSION = 42;
const CACHE = `mm-v${VERSION}`;
const SHELL = ['./', './index.html', './class-bible.html', './card-list.json',
               './manifest.webmanifest', './icons/icon-192.png', './icons/icon-512.png'];

self.addEventListener('install', e => e.waitUntil((async () => {
  const c = await caches.open(CACHE);
  // Individually, so one missing file cannot fail the whole install.
  await Promise.all(SHELL.map(u => c.add(u).catch(() => {})));
  await self.skipWaiting();          // don't wait for other tabs to close
})()));

self.addEventListener('activate', e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
  await self.clients.claim();        // take over open pages immediately
})()));

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // fonts: leave to the browser
  const isArt = url.pathname.includes('/art/') && !url.pathname.endsWith('.json');
  e.respondWith(isArt ? cacheFirst(req) : networkFirst(req));
});

async function networkFirst(req){
  const cache = await caches.open(CACHE);
  try {
    // no-store bypasses the HTTP cache, so a fresh deploy is never masked by it
    const fresh = await fetch(req, { cache: 'no-store' });
    if (fresh && fresh.ok) cache.put(req, fresh.clone());
    return fresh;
  } catch (err) {
    const hit = await cache.match(req)
             || (req.mode === 'navigate' ? await cache.match('./index.html') : null);
    if (hit) return hit;
    throw err;
  }
}

async function cacheFirst(req){
  const cache = await caches.open(CACHE);
  const hit = await cache.match(req);
  if (hit) return hit;
  const fresh = await fetch(req);
  if (fresh && fresh.ok) cache.put(req, fresh.clone());
  return fresh;
}
