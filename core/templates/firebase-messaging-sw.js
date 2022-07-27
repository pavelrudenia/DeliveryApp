importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

firebase.initializeApp({
 apiKey: "AIzaSyAMkOJLD0e9S3vLUsoZxkx6qK4o0RVV2g8",
  authDomain: "deliveryapp-b24e4.firebaseapp.com",
  projectId: "deliveryapp-b24e4",
  storageBucket: "deliveryapp-b24e4.appspot.com",
  messagingSenderId: "313442461491",
  appId: "1:313442461491:web:573e5368806c3742b48046"
});

const messaging = firebase.messaging();