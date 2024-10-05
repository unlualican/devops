# ilk olarak :  Angular app'i build edelim 
FROM node:18-alpine AS build

WORKDIR /app

# json paketini ve lock u nu kopyaladım ve npm install yaptım 
COPY package.json package-lock.json ./
RUN npm install

# geri kalan dosyaları kopyaladım 
COPY . .

# build ediyoruz ,Build sonrası /app/dist içeriklerini listeliyorum ki bu şekilde nginx in html pathine angularin pathini doğru kopyalayim :)
RUN npm run build && ls -la /app/dist/angular-conduit/browser/



# ikinci adım nginx ile publish etmek için 
FROM nginx:alpine

# build app den çıkan dist pathini nginxin html pathine verdim yayınlamak için 
COPY --from=build /app/dist/angular-conduit/browser/ /usr/share/nginx/html


EXPOSE 80

#  NGINX server i başlat komutu 
CMD ["nginx", "-g", "daemon off;"]
