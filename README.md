# Test Task

## Contents.
1  [How deploy project](https://github.com/kykyryzik/Test#-1-Deploy-Manual)

2  [Testing]()
 
## 1 Deploy Manual

### 1.1 How to copy a project.
```
git clone https://github.com/kykyrzik/Test.git
```

### 1.2 Env-file.

```
Rename .env_example to .env and set your values.

DB_HOST=database
DB_PASSWORD=youdbpassword
DB_USER=youdbuser
DB_NAME=youdbname
DB_PORT=youdbport
DB_URI="postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
REDIS_HOST=redis
REDIS_PORT=youdbport
REDIS_URI="redis://{host}:{port}?decode_responses=True"
```

### 1.3 Issue RSA private key + public key pair
Ubuntu/Debian:
```
sudo apt update
sudo apt-get install ssl-cert openssl    
```
Fedora/RHEL/CentOS
```
sudo yum update
sudo yum install openssl
```
```
mkdir .certs
cd .certs
openssl genrsa -out jwt-private.pem 2048
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
 
```

### 1.4 Run a project

Go to your working directory and enter the command:
```
    docker compose up
```

The documentation is available at:

```
http://localhost:8001/docs.
```


## 2 Testing

### 2.1 post endpoint: create user
The password must have Latin letters in upper and lower case,
special characters and numbers.

``` 
{
  "password": "string",
  "email": "user@example.com",
  "referrer": "string" # Optional None
}
```

### 2.2 Authorize
Repeat the data that was created when creating the user for successful authorization

### 2.3 get endpoint: ref
enter the email of the authorized user

You get ref code. Which is stored in-memory bd.

The lifetime of the referral code is 500 seconds

### 2.4 create a new user using the referral code
Upon successful user creation, you will see your referral's email address in the referrer field

