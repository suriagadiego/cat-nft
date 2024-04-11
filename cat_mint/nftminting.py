# from thirdweb import ThirdwebSDK
# from thirdweb.types.nft import NFTMetadataInput
# import os
# from dotenv import load_dotenv

# load_dotenv()


# def mint_nft(cat_info, image_url):
#     # Learn more about securely accessing your private key: https://portal.thirdweb.com/web3-sdk/set-up-the-sdk/securing-your-private-key
#     PRIVATE_KEY = os.environ["PRIVATE_KEY"]

#     # Set the network you want to operate on, or add your own RPC URL here
#     NETWORK = "https://80002.rpc.thirdweb.com"

#     # Finally, you can create a new instance of the SDK to use
#     sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, NETWORK)

#     # Instantiate a new NFT Collection contract as described above.
#     NFT_COLLECTION_ADDRESS = os.environ["NFT_COLLECTION_ADDRESS"]
#     nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)


#     nft_collection.mint(NFTMetadataInput.from_json({
#         "name": cat_info["cat_name"],
#         "description": f"{cat_info['description']} Minted with the Python SDK!",
#         "image": image_url
#     }))

#     return


