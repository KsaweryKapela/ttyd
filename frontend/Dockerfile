FROM node:latest

WORKDIR /app/src

COPY package*.json ./

RUN npm install

COPY . .

WORKDIR /app/src

CMD ["npx", "vite", "--port", "3000", "--host"]
