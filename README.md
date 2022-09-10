# gui-pi
nice touchscreen gui for the pi

### idk what direction this will take tbh
I initially used this as a controller for my fishtank then decided it is pretty versatile and could be used for access control of the garage and gates 

### Features
* A base GUI with status, error reporting, and some buttons
* Python modules which can do Things - such as reading pins, outputting pins, HTTP calls...
* Separation of business from pretty, the business end should have the basic functions in, with the GUI stuff being separate so that it's easy to pull apart

### Expectations
* The business code will be separate to the GUI code
* The business code won't be run by itself - it'll be imported by the GUI code
* As well as GUI stuff, there can be a blank class for use with a LCD/buttons/headless which consumes the business code
* it's all python and modules
* I'm not going to make this super generic or I'll tie myself in knots instead of making something useful
* If you'd like to clone and make this work for you, knock yourself out :D 
