step 1 : Create Django project
step 2 : Push to github repository
step 3 : go into action, create new workflow and all following
[here branch is main]

name: CI/CD Pipeline

on:
  push:
    branches:
      - main  # Trigger the workflow on a push to the 'main' branch

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Tests
      run: |
        python manage.py migrate
        python manage.py test

    - name: Set up SSH
      run: |
        mkdir -p ~/.ssh
        echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
        chmod 600 ~/.ssh/id_rsa
        ssh-keyscan -H ${{ secrets.SSH_HOST }} >> ~/.ssh/known_hosts

    - name: Test SSH Connection
      env:
        SSH_USER: ${{ secrets.SSH_USER }}
        SSH_HOST: ${{ secrets.SSH_HOST }}
      run: |
        ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no $SSH_USER@$SSH_HOST "echo 'SSH connection successful'"

    - name: Deploy to DigitalOcean
      env:
        SSH_USER: ${{ secrets.SSH_USER }}
        SSH_HOST: ${{ secrets.SSH_HOST }}
      run: |
        ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no $SSH_USER@$SSH_HOST << 'EOF'
          cd /root/democicd/CICD1/myproject
          git pull origin main
          source demoenv/bin/activate
          pip install -r requirements.txt
          python manage.py migrate
          sudo systemctl restart gunicorn
          sudo systemctl restart nginx
        EOF

step 4: In Settings > Secrets and variables > actions > new repository secret 
add 3 values,
    a. SSH_USER : ip address
    b. SSH_HOST  : root
    c. SSH_PRIVATE_KEY : 


step 5: deploy django project on ubuntu server using ngnix and gunicorn 

 