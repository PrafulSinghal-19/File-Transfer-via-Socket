### HOW TO GENERATE CERTICIFATE
```cd server```
##### CREATE A PRIVATE KEY
```openssl genrsa -aes256 -out key.pem 2048```
##### GENERATE A SIGN REQUEST
```req -new -key key.pem -out signreq.csr```
##### GENERATE THE CERTIFICATE
```IP_ADDR= IP ADDRESS OF THE SERVER```

```openssl x509 -req -days 365 -extfile <(printf "subjectAltName=IP:$IP_ADDR") -in signreq.csr -signkey key.pem -out certificate.pem```

##### COPY THE CERTIFICATE TO CLIENT FOLDER
```cp certificate.pem ../client```

