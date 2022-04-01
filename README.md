# Chat_System ~ Centrifugo Real Time Messaging with Django Backend Proxy.
----


[Centrifugo](https://centrifugal.dev/)


## Development 

---

Please install 
- Centfugo and redis (centrifugo uses it).
- Postgress

Note:
- You can use docker for these 3 and you can run this app from vscode Run & Debug Section.

## Deployment 
---
```
docker-compose up
```
Redirect to 
```
localhost:9000/docs

and

localhost:9000/chat
```
you need to create user and take token from docs and than 
you are able to reach app with room name and token.

---
### Informations:
 - You can find centrifugo and nginx config files in config folder.
 - Centrifugo Proxy API's under chat/views.py


</br>
Photos

----

![centrifugo example](./image/centrifugo_example.PNG)

---
UI is taken from one of centrifugo official examples.

</br>

```
MIT License

Copyright (c) 2021 FurkanOzkaya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```