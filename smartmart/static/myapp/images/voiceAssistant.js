// // static/js/voiceAssistant.js
// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning Boss");
//     } else if (hr == 12) {
//         speak("Good Noon Boss");
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon Boss");
//     } else {
//         speak("Good Evening Boss");
//     }
// }

// function initializeAssistant() {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript.toLowerCase();
//     speakThis(transcript);
// }

// recognition.onstart = () => {
//     console.log("Voice recognition activated");
// };

// recognition.onspeechend = () => {
//     console.log("Voice recognition stopped");
//     recognition.start();
// };

// recognition.onerror = (event) => {
//     console.error(event.error);
//     recognition.start();
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine boss, tell me how can I help you";
//     } else if (message.includes('name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open google')) {
//         window.open("https://google.com", "_blank");
//         speech.text = "Opening Google";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('back to previous page')) {
//         window.history.back();
//         speech.text = "Going back to previous page";
//     } else if (message.includes('what is the time')) {
//         const time = new Date().toLocaleTimeString();
//         speech.text = `It is ${time}`;
//     } else if (message.includes('what is today\'s date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric", year: "numeric" });
//         speech.text = `Today's date is ${date}`;
//     } else if (message.includes('calculator')) {
//         window.open('Calculator://');
//         speech.text = "Opening Calculator";
//     }

//     window.speechSynthesis.speak(speech);
// }

// document.addEventListener('DOMContentLoaded', () => {
//     const assistantButton = document.getElementById('assistant-button');
//     if (assistantButton) {
//         assistantButton.addEventListener('click', () => {
//             initializeAssistant();
//         });
//     }
// });


// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning Boss");
//     } else if (hr == 12) {
//         speak("Good noon, {{username}}");
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, {{username}}");
//     } else {
//         speak("Good Evening, {{username}}");
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript.toLowerCase();
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, {{username}}, tell me how can I help you";
//     } else if (message.includes('name')|| message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page')|| message.includes('about')) {
//         window.location.href = "/aboutus/";
//         speech.text = "Opening About page {{username}}";

//     }
//     else if (message.includes('open my orders ') || message.includes('my order')|| message.includes('got to my orders')) {
//         window.location.href = "/user_orders/";
//         speech.text = "Opening your orders page {{username}}";
//     } 
//     else if (message.includes('back to home') || message.includes('back') || message.includes('back to home page')) {
    
//         window.location.href = "/home/";
//         speech.text = "Opening HOME page {{username}}";
//     } 
//     else if (message.includes('back to previous page')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// });


// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, " + username);
//     } else if (hr == 12) {
//         speak("Good noon, " + username);
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, " + username);
//     } else {
//         speak("Good Evening, " + username);
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript.toLowerCase();
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus/";
//         speech.text = "Opening About page " + username;
//     } else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders/";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home') || message.includes('back') || message.includes('back to home page')) {
//         window.location.href = "/home/";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view/";
//         speech.text = "Opening Services page " + username;
//     }  
//     else if (message.includes('open maps page') || message.includes('lets buy') || message.includes('go to maps')) {
//         window.location.href = "/maps/";
//         speech.text = "Opening  maps page " + username;
//     } 
//     else if (message.includes('back to previous page')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// });


// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, " + username);
//     } else if (hr == 12) {
//         speak("Good noon, " + username);
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, " + username);
//     } else {
//         speak("Good Evening, " + username);
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript.toLowerCase();
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus/";
//         speech.text = "Opening About page " + username;
//     } else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders/";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home') || message.includes('back') || message.includes('back to home page')) {
//         window.location.href = "/home/";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view/";
//         speech.text = "Opening Services page " + username;
//     } else if (message.includes('open maps page') || message.includes('lets buy') || message.includes('go to maps')) {
//         window.location.href = "/maps/";
//         speech.text = "Opening maps page " + username;
//     } else if (message.includes('back to previous page')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else if (message.includes('open category')) {
//         const categoryName = message.split('open category ')[1];
//         if (categoryName) {
//             window.location.href = `/display_categories/?name=${categoryName}`;
//             speech.text = `Opening category ${categoryName}`;
//         } else {
//             speech.text = "Please specify a category name";
//         }
//     } else if (message.includes('open product')) {
//         const productName = message.split('open product ')[1];
//         if (productName) {
//             window.location.href = `/display_products/?name=${productName}`;
//             speech.text = `Opening product ${productName}`;
//         } else {
//             speech.text = "Please specify a product name";
//         }
//     } else if (message.includes('open feedback page') || message.includes('feedback')) {
//         window.location.href = "/feedback_view/";
//         speech.text = "Opening Feedback page " + username;
//     } else if (message.includes('open profile page') || message.includes('profile')) {
//         window.location.href = "/profile/";
//         speech.text = "Opening Profile page " + username;
//     } else if (message.includes('logout')) {
//         window.location.href = "/logout/";
//         speech.text = "Logging out " + username;
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// });


// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, " + username);
//     } else if (hr == 12) {
//         speak("Good noon, " + username);
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, " + username);
//     } else {
//         speak("Good Evening, " + username);
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     const transcript = event.results[current][0].transcript.toLowerCase();
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };
// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus/";
//         speech.text = "Opening About page " + username;
//     } else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders/";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home') || message.includes('back') || message.includes('back to home page')) {
//         window.location.href = "/home/";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view/";
//         speech.text = "Opening Services page " + username;
//     } else if (message.includes('open maps page') || message.includes('lets buy') || message.includes('go to maps')) {
//         window.location.href = "/maps/";
//         speech.text = "Opening maps page " + username;
//     } else if (message.includes('back to previous page')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else if (message.includes('open category')) {
//         const parts = message.split('open category ')[1].trim().split(' ');
//         const shopId = parts[0];
//         const categoryName = parts.slice(1).join(' ');

//         if (shopId && categoryName) {
//             window.location.href = `/display_categories/?shopid=${shopId}&name=${categoryName}`;
//             speech.text = `Opening category ${categoryName} in shop ${shopId}`;
//         } else {
//             speech.text = "Please specify a shop ID and category name";
//         }
//     }  else if (message.includes('open product')) {
//         const productName = message.split('open product ')[1].trim();
        
//         if (productName) {
//             window.location.href = `/display_products/?name=${productName}`;
//             speech.text = `Opening product ${productName}`;
//         } else {
//             speech.text = "Please specify a product name";
//         }
//     } else if (message.includes('open feedback page') || message.includes('feedback')) {
//         window.location.href = "/feedback/";
//         speech.text = "Opening Feedback page " + username;
//     } else if (message.includes('open profile page') || message.includes('profile')) {
//         window.location.href = "/profile/";
//         speech.text = "Opening Profile page " + username;
//     } else if (message.includes('logout')) {
//         window.location.href = "/logout/";
//         speech.text = "Logging out " + username;
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }


// window.addEventListener('load', () => {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// // });
// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, " + username);
//     } else if (hr == 12) {
//         speak("Good noon, " + username);
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, " + username);
//     } else {
//         speak("Good Evening, " + username);
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     let transcript = event.results[current][0].transcript.toLowerCase();
    
//     // Remove trailing punctuation
//     transcript = transcript.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").trim();
    
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus";
//         speech.text = "Opening About page " + username;
//     } else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home') || message.includes('back') || message.includes('back to home page')) {
//         window.location.href = "/home";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view";
//         speech.text = "Opening Services page " + username;
//     } else if (message.includes('open maps page') || message.includes('lets buy') || message.includes('go to maps')) {
//         window.location.href = "/maps";
//         speech.text = "Opening maps page " + username;
//     } else if (message.includes('back to previous page')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } else if (message.includes('open instagram')) {
//         window.open("https://instagram.com", "_blank");
//         speech.text = "Opening Instagram";
//     } else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else if (message.includes('open category')) {
//         const parts = message.split('open category ')[1].trim().split(' ');
//         const shopId = parts[0];
//         const categoryName = parts.slice(1).join(' ');

//         if (shopId && categoryName) {
//             window.location.href = `/display_categories/?shopid=${shopId}&name=${categoryName}`;
//             speech.text = `Opening category ${categoryName} in shop ${shopId}`;
//         } else {
//             speech.text = "Please specify a shop ID and category name";
//         }
//     }  else if (message.includes('open product')) {
//         const productName = message.split('open product ')[1].trim();
        
//         if (productName) {
//             window.location.href = `/display_products/?name=${productName}`;
//             speech.text = `Opening product ${productName}`;
        
//         }
//          else {
//             speech.text = "Please specify a product name";
//         }
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     speak("Activating SmartMart Assistant");
//     speak("Going online");
//     wishMe();
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// });


// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, " + username);
//     } else if (hr == 12) {
//         speak("Good noon, " + username);
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, " + username);
//     } else {
//         speak("Good Evening, " + username);
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     let transcript = event.results[current][0].transcript.toLowerCase();
    
//     // Remove trailing punctuation
//     transcript = transcript.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").trim();
    
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus";
//         speech.text = "Opening About page " + username;
//     }else if (message.includes('open my profile') || message.includes('my account') || message.includes('go to my account')|| message.includes('go to my profile')) {
//         window.location.href = "/profile";
//         speech.text = "Opening your profile page " + username;
//     }
//      else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home')  || message.includes('back to home page')) {
//         window.location.href = "/home";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view";
//         speech.text = "Opening Services page " + username;
//     } else if (message.includes('open maps page') || message.includes('lets buy') || message.includes('go to maps')|| message.includes('continue shoping')) {
//         window.location.href = "/maps";
//         speech.text = "Opening maps page " + username;
//     } else if (message.includes('back to previous page')|| message.includes('back')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } 
//      else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//     } else if (message.includes('open category')) {
//         const parts = message.split('open category ')[1].trim().split(' ');
//         const shopId = parts[0];
//         const categoryName = parts.slice(1).join(' ');

//         if (shopId && categoryName) {
//             window.location.href = `/display_categories/?shopid=${shopId}&name=${categoryName}`;
//             speech.text = `Opening category ${categoryName} in shop ${shopId}`;
//         } else {
//             speech.text = "Please specify a shop ID and category name";
//         }
//     } else if (message.includes('open product')) {
//         const productName = message.split('open product ')[1].trim();

//         if (productName) {
//             window.location.href = `/display_products/?name=${productName}`;
//             speech.text = `Opening product ${productName}`;
//         } else {
//             speech.text = "Please specify a product name";
//         }
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     if (!welcomeSpoken) {
//         speak("Activating SmartMart Assistant");
//         speak("Going online");
//         wishMe();
//         // Set welcome_spoken flag to true in session storage
//         sessionStorage.setItem('welcome_spoken', 'true');
//     }
//     if (errorMessage) {
//         speak(errorMessage);
//     }
//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// // });
// const btn = document.querySelector('.talk');
// const content = document.querySelector('.content');

// function speak(sentence) {
//     const text_speak = new SpeechSynthesisUtterance(sentence);
//     text_speak.rate = 1;
//     text_speak.pitch = 1;
//     window.speechSynthesis.speak(text_speak);
// }

// function wishMe() {
//     var day = new Date();
//     var hr = day.getHours();

//     if (hr >= 0 && hr < 12) {
//         speak("Good Morning, Boss");
//     } else if (hr == 12) {
//         speak("Good noon,  Boss");
//     } else if (hr > 12 && hr <= 17) {
//         speak("Good Afternoon, Boss");
//     } else {
//         speak("Good Evening,  Boss");
//     }
// }

// const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// const recognition = new SpeechRecognition();

// let assistantActive = true;

// recognition.onresult = (event) => {
//     const current = event.resultIndex;
//     let transcript = event.results[current][0].transcript.toLowerCase();
    
//     // Remove trailing punctuation
//     transcript = transcript.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").trim();
    
//     content.textContent = transcript;
//     speakThis(transcript);
// };

// recognition.onend = () => {
//     if (assistantActive) {
//         recognition.start();
//     }
// };

// function speakThis(message) {
//     const speech = new SpeechSynthesisUtterance();
//     speech.text = "I did not understand what you said, please try again";

//     if (message.includes('hey') || message.includes('hello')) {
//         speech.text = "Hello Boss, this is SmartMart";
//     } else if (message.includes('how are you')) {
//         speech.text = "I am fine, " + username + ", tell me how can I help you";
//     } else if (message.includes('name') || message.includes('what is your name')) {
//         speech.text = "My name is SmartMart voice Assistant";
//     } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
//         window.location.href = "/aboutus";
//         speech.text = "Opening About page " + username;
//     }else if (message.includes('open my profile') || message.includes('my account') || message.includes('go to my account')|| message.includes('go to my profile')) {
//         window.location.href = "/profile";
//         speech.text = "Opening your profile page " + username;
//     }
//      else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
//         window.location.href = "/user_orders";
//         speech.text = "Opening your orders page " + username;
//     } else if (message.includes('back to home')  || message.includes('back to home page')) {
//         window.location.href = "/home";
//         speech.text = "Opening HOME page " + username;
//     } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
//         window.location.href = "/services_view";
//         speech.text = "Opening Services page " + username;
//     }else if (message.includes('open feedback page') || message.includes('go to feedback') || message.includes('feedback')) {
//         window.location.href = "/feedback_view";
//         speech.text = "Opening feedbback page " + username;
//     }  else if (message.includes('log out') || message.includes('sign out')) {
//         window.location.href = "/logout";
//         speech.text = "thank you for using Smartmart i wish you to come again " + username;
//     } 
//     else if (message.includes('open maps page') || message.includes('continue shopping') || message.includes('go to maps')|| message.includes('continue shoping')) {
//         window.location.href = "/maps";
//         speech.text = "Opening maps page " + username;
//     } else if (message.includes('back to previous page')|| message.includes('back')) {
//         history.back();
//         speech.text = "Going back to the previous page";
//     } 
//     else if (message.includes('help')|| message.includes('help me')|| message.includes('how can use this')|| message.includes('not understanding')) {
//         speech.text = "To order products in SmartMart, first register, then login. Go to maps and select any one of the nearby shops. Then select categories and products. Download the invoice and proceed to payment. You can choose online, offline, or cash on delivery. Finally, place your order.";
//     } 
//      else if (message.includes('time')) {
//         const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
//         speech.text = time;
//     } else if (message.includes('date')) {
//         const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
//         speech.text = date;
//     } else if (message.includes('stop assistant')) {
//         assistantActive = false;
//         recognition.stop();
//         speech.text = "Assistant stopped";
//         window.location.href = "/home";
//     } else if (message.includes('open category')) {
//         const parts = message.split('open category ')[1].trim().split(' ');
//         const shopId = parts[0];
//         const categoryName = parts.slice(1).join(' ');

//         if (shopId && categoryName) {
//             window.location.href = `/display_categories/?shopid=${shopId}&name=${categoryName}`;
//             speech.text = `Opening category ${categoryName} in shop ${shopId}`;
//         } else {
//             speech.text = "Please specify a shop ID and category name";
//         }
//     } else if (message.includes('open product')) {
//         const productName = message.split('open product ')[1].trim();

//         if (productName) {
//             window.location.href = `/display_products/?name=${productName}`;
//             speech.text = `Opening product ${productName}`;
//         } else {
//             speech.text = "Please specify a product name";
//         }
//     } else {
//         speech.text = "I did not understand what you said, please try again";
//     }

//     speech.volume = 1;
//     speech.pitch = 1;
//     speech.rate = 1;

//     window.speechSynthesis.speak(speech);
// }

// window.addEventListener('load', () => {
//     const welcomeSpoken = sessionStorage.getItem('welcome_spoken') == 'true';
//     const errorMessage = sessionStorage.getItem('error_message');

//     if (!welcomeSpoken) {
//         speak("Activating SmartMart Assistant");
//         speak("Going online");
//         wishMe();
//         sessionStorage.setItem('welcome_spoken', 'true');
//     }
//     else{
//         speak("how can i help you, Boss");
//     }

//     if (errorMessage) {
//         speak(errorMessage);
//         sessionStorage.removeItem('error_message');
//     }

//     recognition.start();
// });

// btn.addEventListener('click', () => {
//     recognition.start();
// });


const btn = document.querySelector('.talk');
const content = document.querySelector('.content');

function speak(sentence) {
    const text_speak = new SpeechSynthesisUtterance(sentence);
    text_speak.rate = 1;
    text_speak.pitch = 1;
    window.speechSynthesis.speak(text_speak);
}

function wishMe() {
    var day = new Date();
    var hr = day.getHours();

    if (hr >= 0 && hr < 12) {
        speak("Good Morning, Boss");
    } else if (hr == 12) {
        speak("Good noon, Boss");
    } else if (hr > 12 && hr <= 17) {
        speak("Good Afternoon, Boss");
    } else {
        speak("Good Evening, Boss");
    }
}

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

let assistantActive = true;

recognition.onresult = (event) => {
    const current = event.resultIndex;
    let transcript = event.results[current][0].transcript.toLowerCase();
    
    // Remove trailing punctuation
    transcript = transcript.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").trim();
    
    content.textContent = transcript;
    speakThis(transcript);
};

recognition.onend = () => {
    if (assistantActive) {
        recognition.start();
    }
};

function speakThis(message) {
    const speech = new SpeechSynthesisUtterance();
    speech.text = "I did not understand what you said, please try again";

    if (message.includes('hey') || message.includes('hello')) {
        speech.text = "Hello Boss, this is SmartMart";
    } else if (message.includes('how are you')) {
        speech.text = "I am fine, " + username + ", tell me how can I help you";
    } else if (message.includes('name') || message.includes('what is your name')) {
        speech.text = "My name is SmartMart voice Assistant";
    } else if (message.includes('open about page') || message.includes('go to about page') || message.includes('about')) {
        window.location.href = "/aboutus";
        speech.text = "Opening About page " + username;
    } else if (message.includes('open my profile') || message.includes('my account') || message.includes('go to my account') || message.includes('go to my profile')) {
        window.location.href = "/profile";
        speech.text = "Opening your profile page " + username;
    } else if (message.includes('open my orders') || message.includes('my order') || message.includes('go to my orders')) {
        window.location.href = "/user_orders";
        speech.text = "Opening your orders page " + username;
    }else if (message.includes('track order') || message.includes('track  orders')) {
        window.location.href = "/track_order";
        speech.text = "Opening your oTrack order page " + username;
    }
     else if (message.includes('back to home') || message.includes('back to home page')) {
        window.location.href = "/home";
        speech.text = "Opening HOME page " + username;
    } else if (message.includes('open services page') || message.includes('go to services') || message.includes('services')) {
        window.location.href = "/services_view";
        speech.text = "Opening Services page " + username;
    } else if (message.includes('open feedback page') || message.includes('go to feedback') || message.includes('feedback')) {
        window.location.href = "/feedback_view";
        speech.text = "Opening feedback page " + username;
    } else if (message.includes('log out') || message.includes('sign out')) {
        window.location.href = "/logout";
        speech.text = "Thank you for using SmartMart, I wish you to come again " + username;
    } else if (message.includes('open maps page') || message.includes('continue shopping') || message.includes('go to maps') || message.includes('continue shopping')) {
        window.location.href = "/maps";
        speech.text = "Opening maps page " + username;
    } else if (message.includes('back to previous page') || message.includes('back')) {
        history.back();
        speech.text = "Going back to the previous page";
    } else if (message.includes('help') || message.includes('help me') || message.includes('how can use this') || message.includes('not understanding')) {
        speech.text = "To order products in SmartMart, first register, then login. Go to maps and select any one of the nearby shops. Then select categories and products. Download the invoice and proceed to payment. You can choose online, offline, or cash on delivery. Finally, place your order.";
    } else if (message.includes('time')) {
        const time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
        speech.text = time;
    } else if (message.includes('date')) {
        const date = new Date().toLocaleString(undefined, { month: "short", day: "numeric" });
        speech.text = date;
    } else if (message.includes('stop assistant')) {
        assistantActive = false;
        recognition.stop();
        speech.text = "Assistant stopped";
        window.location.href = "/home";
    } else if (message.includes('open category')) {
        const parts = message.split('open category ')[1].trim().split(' ');
        const shopId = parts[0];
        const categoryName = parts.slice(1).join(' ');

        if (shopId && categoryName) {
            window.location.href = `/display_categories/?shopid=${shopId}&name=${categoryName}`;
            speech.text = `Opening category ${categoryName} in shop ${shopId}`;
        } else {
            speech.text = "Please specify a shop ID and category name";
        }
    }if (message.includes('open product')) {
        const parts = message.split('open product ')[1].trim().split(' ');
        const shopId = parts[0];
        const productName = parts.slice(1).join(' ');
    
        if (shopId && productName) {
            window.location.href = `/display_products/?shop_id=${shopId}&name=${productName}`;
            speech.text = `Opening product ${productName} in shop ${shopId}`;
        } else {
            speech.text = "Please specify a shop ID and product name";
        }
    }
    
    
     else {
        speech.text = "I did not understand what you said, please try again";
    }

    speech.volume = 1;
    speech.pitch = 1;
    speech.rate = 1;

    window.speechSynthesis.speak(speech);
}

window.addEventListener('load', () => {
    const welcomeSpoken = sessionStorage.getItem('welcome_spoken') == 'true';
    const errorMessage = sessionStorage.getItem('error_message');

    if (!welcomeSpoken) {
        speak("Activating SmartMart Assistant");
        speak("Going online");
        wishMe();
        sessionStorage.setItem('welcome_spoken', 'true');
    } else {
        speak("how can I help you, Boss");
    }

    if (errorMessage) {
        speak(errorMessage);
        sessionStorage.removeItem('error_message');
    }

    recognition.start();
});

btn.addEventListener('click', () => {
    recognition.start();
});
