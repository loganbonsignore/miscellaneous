# Kylin Node

## Local Development

Follow these steps to prepare a local development environment :hammer_and_wrench:

### Setup
[Rust development environment](https://substrate.dev/docs/en/knowledgebase/getting-started).


### Build

Checkout code
```bash
git clone --recursive https://github.com/Kylin-Network/kylin-node.git
git checkout polkadot-v0.9.5
```

Build debug version

```bash
cd kylin-node
cargo build
```

Build release version

```bash
cd kylin-node
cargo build --release
```

### Docker

Build debug version

```bash
cd scripts
docker-compose up -d
```

Check if the parachain and relay chains are running.
1. kylin-node should be visible
2. alice, bob & charlie should be visible

```bash
docker ps
``````




### Interact
Using [Kylin Market Front End](https://github.com/Kylin-Network/kylin-market-frontend) which can be used to interact with Kylin Node.

``` bash
git clone https://github.com/Kylin-Network/kylin-market-frontend.git
cd ./kylin-market-frontend
yarn install
```


## Run

### Development Chain

Purge any existing dev chain state:

```bash
./target/debug/kylin-node purge-chain --dev
```

Start a dev chain:

```bash
./target/debug/kylin-node --dev
```

or, start a dev chain with detailed logging:

```bash
RUST_LOG=debug RUST_BACKTRACE=1 ./target/debug/kylin-node -lruntime=debug --dev
```

### Use `release` version

replace `debug` with `release`.

**Caution! Donot try to run `release` version everytime, it will take lots of time.**

### Access the frontend & Setup Sudo Access
1. visit https://<hostname>:3001
2. change endpoint to a custom endpoint replacing localhost with the IP of the machine if you're not running the instance locally.
3. Add an account with a mnemonice seed. Provide an Account and a Password
4. Under Developer tab, the Sudo option will be available


### Genesis & WASM Local Key Files
1. Exec into Docker
```bash
docker exec -ti kylin-node bash
```
2. Browse into cumulus_parachain directory. Any file generated here will automatically appear on the file system and export the keys
```bash
cd cumulus_parachain
export-genesis-state --parachain-id 2013 > para-2013-genesis-local
export-genesis-state --parachain-id 2013 > para-2013-wasm-local
```




### Register the chain
1. Switch custom endpoint to 9944
2. Developer -> Sudo
3. Submit the following change
paraSudoWrapper -> sudoScheduleParaInitializeId
4. Use the paraid of the kylin-node based on the Docker yaml file
5. Copy the exported files (genesis & wasm) out and upload them to the genesisHead (genesis files) and validationCode (wasm file)


### Validate the parachain is registered
1. 



### Using polkadot.js
visit <https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A9944#/settings/developer>.


fill the config in Settings>>Developer.
```js
{
  "Address": "<AccountId>",
  "LookupSource": "<AccountId>",
  "DataInfo": {
    "url": "Text",
    "data": "Text"
  }
}
```

#### Add OCW Signer
Run `./scripts/insert_alice_key.sh` to insert OCW signer. If the OCW signer does not have enough balance, please charge money as following instructions.

#### Add New Oracle Service URL
Select Developer>>Extrinsics, then using priceFetchModule.addFetchDataRequest(url), type a url encode hex format.
![pic](doc/imgs/addFetchDataRequest.png)

#### Query Oracle Data
Select Developer>>Chain state, then using priceFetchModule.requestedOffchainData(u64), press **+**.
![pic](doc/imgs/queryRequestedData.jpg)
