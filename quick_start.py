#!/usr/bin/env python
"""
Quick Start Script for DigitalPro Website
Run this script to set up your website quickly
"""

import os
import sys
import django
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

def setup_django():
    """Setup Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tos.settings')
    django.setup()

def run_migrations():
    """Run database migrations"""
    print("🔄 Running database migrations...")
    try:
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migrations completed successfully!")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

def create_superuser():
    """Create a default superuser if none exists"""
    User = get_user_model()
    if User.objects.filter(is_superuser=True).exists():
        print("👤 Superuser already exists")
        return True
    
    print("👤 Creating default superuser...")
    try:
        user = User.objects.create_superuser(
            username='admin',
            email='admin@digitalpro.com',
            password='admin123'
        )
        print("✅ Superuser created successfully!")
        print(f"   Username: admin")
        print(f"   Password: admin123")
        print(f"   Email: admin@digitalpro.com")
        print("⚠️  Please change the password after first login!")
        return True
    except Exception as e:
        print(f"❌ Superuser creation failed: {e}")
        return False

def check_requirements():
    """Check if all required packages are installed"""
    print("🔍 Checking requirements...")
    required_packages = [
        'django',
        'pillow',  # for image handling
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - MISSING")
    
    if missing_packages:
        print(f"\n📦 Install missing packages:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All required packages are installed!")
    return True

def main():
    """Main setup function"""
    print("🚀 DigitalPro Website Quick Start")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please install missing packages first")
        return
    
    # Setup Django
    setup_django()
    
    # Run migrations
    if not run_migrations():
        print("\n❌ Setup failed at migrations step")
        return
    
    # Create superuser
    if not create_superuser():
        print("\n❌ Setup failed at superuser creation step")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Start the server: python manage.py runserver")
    print("2. Go to: http://127.0.0.1:8000/admin/")
    print("3. Login with admin/admin123")
    print("4. Start adding your company content!")
    print("\n📚 Check SETUP_GUIDE.md for detailed instructions")

if __name__ == '__main__':
    main()
