# Decentralized Generational Identity (DGI)

## Overview
**Decentralized Generational Identity (DGI)** is a blockchain-based platform that securely manages family identities and legacy data through smart contracts and decentralized file storage. By leveraging technologies like **Polygon**, **IPFS**, and **Zero-Knowledge Proofs (ZKP)**, DGI ensures privacy, transparency, and data ownership.

---

## Features
- **Family-Based Identity Validation**: Family members validate identities through a decentralized protocol.
- **Secure File Sharing**: Files are uploaded to IPFS and accessed securely via blockchain permissions.
- **Zero-Knowledge Proofs**: Enables private identity and access verification.
- **Scalable Transactions**: Built on **Polygon**, offering low-cost and high-speed transactions.

---

## Tech Stack
### **Smart Contracts**
- **Solidity**
- **Polygon (Layer 2)**
- **Ethereum Virtual Machine (EVM)**

### **Frontend**
- **Next.js** (React Framework)
- **MetaMask Wallet Integration**

### **File Storage**
- **IPFS (InterPlanetary File System)**

---

## Installation

### Prerequisites
1. **Node.js (>=14.x)**
2. **Foundry** for smart contract testing and deployment:
   ```bash
   curl -L https://foundry.paradigm.xyz | bash
   foundryup
   ```
3. **MetaMask Wallet** installed in your browser.
4. RPC Endpoint (e.g., Polygon Testnet or Anvil).

---

### Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/DGI.git
cd DGI
```

#### 2. Set Up Smart Contracts

##### a) Install Foundry
```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

##### b) Build and Test Contracts
```bash
forge build
forge test
```

##### c) Deploy Contracts
1. Start a local blockchain environment with **Anvil**:
   ```bash
   anvil
   ```
2. Deploy the contract:
   ```bash
   forge script script/Deploy.s.sol --broadcast --rpc-url http://localhost:8545
   ```

#### 3. Set Up Frontend (Next.js)

##### a) Navigate to the Frontend Directory
```bash
cd frontend
```

##### b) Install Dependencies
```bash
npm install
```

##### c) Run the Application
```bash
npm run dev
```
Access the app at [http://localhost:3000](http://localhost:3000).

---

## File Upload via IPFS
We use **IPFS-http-client** to handle decentralized file uploads.

### Steps to Upload
1. Select a file using the Next.js frontend.
2. The file is uploaded to IPFS via the `ipfs.js` utility.
3. The IPFS hash is returned and stored on the blockchain.

---

## Testing

### Smart Contract Tests
Run Foundry tests:
```bash
forge test
```

### Frontend Testing
1. Open [http://localhost:3000](http://localhost:3000).
2. Connect your wallet via MetaMask.
3. Test features like file uploads and smart contract interactions.

---

## Contribution
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git push origin feature-name
   ```
4. Submit a Pull Request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Troubleshooting

### Common Issues
1. **MetaMask Wallet Doesn't Connect**:
   - Ensure MetaMask is installed and connected to the correct network.
   - Check RPC URL settings.

2. **IPFS Upload Fails**:
   - Verify the IPFS endpoint in `frontend/utils/ipfs.js`.

3. **Deployment Issues**:
   - Ensure **Anvil** is running or the correct testnet RPC URL is configured.

---

Thank you for supporting **Decentralized Generational Identity (DGI)**! 🚀
