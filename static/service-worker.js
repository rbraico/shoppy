const CACHE_NAME = 'shoppy-cache-v1';
const urlsToCache = [
  '/',
  '/shopping_list',
  '/static/style.css',
  '/static/script.js'
];

// Installazione
self.addEventListener('install', event => {
  console.log('[Service Worker] Install');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch intercettato
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
