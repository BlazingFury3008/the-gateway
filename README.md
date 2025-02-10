# the-gateway
The Gateway Website
# Running the Test Server

## Prerequisites
Before running the test server, ensure that you have the following installed:
- **Node.js & npm** (for the frontend)
- **Python** (for the backend)
- **MySQL Server** (for database management)

## Setting Up the Frontend
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install the required dependencies:
   ```sh
   npm install
   ```

## Setting Up the Backend
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment (Windows users):
   ```sh
   venv.bat
   ```
3. Activate the virtual environment:
   ```sh
   venv\Scripts\activate
   ```
   For macOS/Linux users, use:
   ```sh
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setting Up the Database
1. Ensure MySQL Server is running.
2. Use the setup script to configure the database:
   ```sh
   mysql -u root -p < MySQL_Server_Setup/setup.sql
   ```

## Creating the Environment Configuration
The backend requires a `.env` file in the `backend` directory with the following contents:
```ini
DATABASE_URL="mysql+pymysql://root:Dasher123%40bc@localhost/fastapi_db"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES="30"
```
### Explanation of Environment Variables
- **DATABASE_URL**: Connection string for the MySQL database using `pymysql`.
- **SECRET_KEY**: A secret key used for signing JWT tokens and securing authentication.
- **ALGORITHM**: The hashing algorithm used for encoding JWT tokens.
- **ACCESS_TOKEN_EXPIRE_MINUTES**: Specifies the expiration time (in minutes) for access tokens.

## Running the Servers
### Running the Backend
Start the FastAPI backend using:
```sh
run.bat
```

### Running the Frontend
Start the Next.js frontend:
```sh
npm run dev
```

## Accessing the Application
- **Frontend**: Visit `http://localhost:3000`
- **Backend (API Docs)**: Visit `http://localhost:8000/docs`

## Building and Deploying the Project
### Building the Frontend
To generate a production build of the frontend:
```sh
npm run build
```

### Deploying the Frontend
Deploy the built frontend to a hosting service such as Vercel, Netlify, or a custom server.

### Deploying the Backend
1. Ensure the backend dependencies are installed.
2. Run the backend on a production server using:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```
3. Use a process manager like `pm2` or `systemd` for uptime management.

You're now ready to build and deploy the project!

