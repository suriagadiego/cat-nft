# Cat Minter

### Turn your furry friend into a purr-fectly unique NFT!

Cat Minter is a full-stack web application built with Django (backend) and React (frontend) that empowers you to immortalize your feline companion on the blockchain as a one-of-a-kind Non-Fungible Token (NFT).


### Access APIs on the cloud or local:

## Sign up
This API allows users to register for the app. Upon successful registration, a UUID is generated and assigned to the user for owner and cat and record-keeping.

** POST ** apiendpoint/user/create/

### Request Body
| **Name**     | **Type** | **Description**                       |
|--------------|----------|---------------------------------------|
| first_name   | string   | Your first name                       |
| last_name    | string   | Your last name                        |
| email        | string   | Your Email                            |
| password     | string   | secure password                       |
| is_superuser | bool     | (OPTIONAL) if account is admin |

### Response 201
```json
{
    "id": 4,
    "first_name": "Diego",
    "last_name": "Suriaga",
    "email": "dom@admin.com",
    "is_superuser": true
}

```

## Login
This API allows user to login. Logins are required to view and register your cats for NFT Minting.

** POST ** apiendpoint/user/login/

### Request Body
| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| email    | string   | your email      |
| password | string   | secure password |

### Response 200
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjkxMDY0OCwiaWF0IjoxNzEyODI0MjQ4LCJqdGkiOiJhMjA1NDIzMTk3MmU0MTIzOWM3NmE1YjkwOGU3NGRhZSIsInVzZXJfaWQiOjF9.ytapwF_ivcLrEw23FeXRMdizJGCPB01S8ZbDzCR3cZM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyODI3ODQ4LCJpYXQiOjE3MTI4MjQyNDgsImp0aSI6ImJlZWNjMDBiOGMzMTRhOWFhNTUyNTMwYTY3ODhkNTA5IiwidXNlcl9pZCI6MX0.QPVSjr7T3WGR9871WVC0f0inrHLu4SkC0PaQ7r4d1jA"
}
```

## Get all of your Cats
This API endpoint returns a list of all your cat NFTs. With this endpoint, you can easily retrieve and manage your collection of unique feline companions on the blockchain.

** GET ** apiendpoint/mint/list_of_my_cats/
### Request Params
| **Name** | **Type** | **Description**                                             |
|----------|----------|-------------------------------------------------------------|
| cat_name | string   | filter params case insensitive and uses icontains           |
| owner    | string   | filter params case insensitive and uses icontains           |
| sort_by  | string   | sort using an identifier. E.g. "cat_name" or "-cat_name" for desc |


### Response 200
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "uuid": "09279216-5d42-49ad-8741-759bf2265bee",
            "cat_name": "CutiePie",
            "description": "kitten found in the dumpster lmao",
            "breed": "puspin",
            "image_url": null,
            "owner": 1,
            "created_at": "2024-04-10T15:37:16.356688Z",
            "updated_at": "2024-04-10T15:37:16.356663Z"
        }
    ]
}
```
## Register cat information
This API endpoint empowers you to immortalize your furry friend on the blockchain! Craft a one-of-a-kind Cat NFT, showcasing the majesty and personality of your feline companion.

### Request Body

| **Name**    | **Type** | **Description**              |
|-------------|----------|------------------------------|
| cat_name    | string   | Name of your furry friend    |
| breed       | string   | Their breed                  |
| description | string   | Describe your furry friend   |
| image_url   | string   | url of a picture of your cat |


### Response 201
```json
{
    "id": 8,
    "uuid": "31bab983-1dd1-46b0-9962-7f9fbe12d4b0",
    "cat_name": "Mocha",
    "description": "neighborhood cat",
    "breed": "Siamese",
    "updated_at": "2024-04-11T08:44:57.619696Z",
    "created_at": "2024-04-11T08:44:57.619710Z",
    "image": 9,
    "owner": 1
}
```


## Update cat information
This API endpoint allows you to modify the details associated with a specific cat NFT in your collection.
*This api only edits the data registered through the database not in the blockchain*

** PUT ** apiendpoint/mint/list_of_my_cats/

### Request Body
| **Name**    | **Type** | **Description**              |
|-------------|----------|------------------------------|
| cat_name    | string   | Name of your furry friend    |
| breed       | string   | Their breed                  |
| description | string   | Describe your furry friend   |
| image_url   | string   | url of a picture of your cat |

### Response 200
{
    "id": 8,
    "uuid": "31bab983-1dd1-46b0-9962-7f9fbe12d4b0",
    "cat_name": "Mocha Updated",
    "description": "neighborhood cat",
    "breed": "siamese",
    "updated_at": "2024-04-11T08:45:32.619696Z",
    "created_at": "2024-04-11T08:44:57.619710Z",
    "image": 9,
    "owner": 1
}

## NFT Minting Steps
**NFT Minting is Developed using Thirdweb Typescript SDK**
*Tried developing using Python SDK but it's been depracated*

```
import { ThirdwebSDK } from "@thirdweb-dev/sdk";

async function main() {
  const NETWORK = "mumbai";
  // Learn more about securely accessing your private key: https://portal.thirdweb.com/web3-sdk/set-up-the-sdk/securing-your-private-key
  const sdk = ThirdwebSDK.fromPrivateKey("<your-private-key-here>", NETWORK);

  const deployedAddress = await sdk.deployer.deployNFTCollection({
    name: "My NFT Collection",
    primary_sale_recipient: "0x-your-public-wallet-address-here",
  });
  console.log(deployedAddress);

  // here, we'll add minting of NFTs in the next step.
}

main();


const nftCollection = sdk.getNFTCollection(deployedAddress);

const nft = await nftCollection.mintTo("0x-your-public-wallet-address-here", {
  name: "My NFT",
});

console.log(nft);
```

## Demo
this is the video

## Cloning the Backend Service
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/suriagadiego/stray_api.git 

2. Create a virtual environment (recommended) and activate it.

    ```bash
    pipenv shell
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Get env file from email <br>
*Or create your own database and own env file on the root of the project with these values*

    ```
    PGDATABASE=
    PGUSER=
    PGPASSWORD=
    PGHOST=
    PGPORT=
    ```
