FROM node:16

WORKDIR /usr/src/apa

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]