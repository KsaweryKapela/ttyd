#make a file called Docker
FROM node:latest

#sets a folder
RUN mkdir -p /app/src

#sets working directory
WORKDIR /app/src

#copy the package
COPY package.json .

#runs npm install
RUN npm install

COPY . .

#runs the comand npm start
CMD ["npx", "vite", "--port", "3000", "--host"]
