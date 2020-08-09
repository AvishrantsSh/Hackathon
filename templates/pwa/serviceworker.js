
const CACHE = 'cache_v1';
const filestoCache = ['/static/noconn.html',
                      '/static/style/basestyle.css',
                      '/manifest.json',
                      '/static/images/assets/Avishrant.jpg',
                      '/static/images/assets/Kunal.jpg',
                      '/static/images/assets/Prateek.jpg',
                      '/static/images/assets/Pushpdeep.jpg',
                      '/static/images/icons/avatar.svg',
                      '/static/images/icons/avatar.png',
]
const offlineURL = ['/static/noconn.html']

self.addEventListener('install', function(event) {
  console.log('The service worker is being installed.');
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE).then(function(cache) {
      
      return cache.addAll(filestoCache);
    })
  );
});


self.addEventListener('activate', (e) => {
  self.skipWaiting();

  e.waitUntil(
    caches.keys().then((keyList) => {
          return Promise.all(keyList.map((key) => {
        if(key !== CACHE) {
          return caches.delete(key);
        }
      }));
    })
  );
});

self.addEventListener('fetch', function(event) {

     event.respondWith(
      caches.match(event.request).then(response => {
        if (response) {
          console.log('Found ', event.request.url, ' in cache');
          return response;
        }
        console.log('Network request for ', event.request.url);
        return fetch(event.request)

      }).catch(function(err) {
        // Fallback to cache
        console.log("Oh Snap :" + err);
        return caches.match(offlineURL)
    })
    );
});

