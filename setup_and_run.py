#!/usr/bin/env python3
"""
Smart Crop Recommendation System - Setup and Run Script
This script helps set up and launch the crop recommendation system.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_files():
    """Check if all required files exist"""
    required_files = [
        "app.py",
        "crop_data.py", 
        "crop_model.pkl",
        "templates/index.html",
        "requirements.txt"
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"  ✅ {file}")
    
    if missing_files:
        print("\n❌ Missing required files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    print("✅ All required files present!")
    return True

def run_application():
    """Launch the Flask application"""
    print("\n🚀 Starting the Smart Crop Recommendation System...")
    print("📍 The application will be available at: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped. Thank you for using the Smart Crop Recommendation System!")

def main():
    """Main setup and run function"""
    print("🌱 Smart Crop Recommendation System - Setup & Launch")
    print("=" * 60)
    
    # Check if all required files exist
    if not check_files():
        print("\n❌ Cannot proceed without required files. Please ensure all files are present.")
        return
    
    # Install requirements
    print("\n" + "=" * 60)
    if not install_requirements():
        print("\n❌ Failed to install requirements. Please install manually using:")
        print("   pip install -r requirements.txt")
        return
    
    # Run the application
    print("\n" + "=" * 60)
    run_application()

if __name__ == "__main__":
    main()