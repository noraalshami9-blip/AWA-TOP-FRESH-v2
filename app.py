from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#D32F2F">
    <title>TOP FRESH</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;900&display=swap');

        :root {
            --primary: #D32F2F;
            --accent: #FF6B00;
            --dark: #1A1A1A;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Cairo', sans-serif;
            background: #fff;
            color: #333;
            overflow-x: hidden;
        }

        header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(26, 26, 26, 0.98);
            backdrop-filter: blur(12px);
            z-index: 1000;
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 2.2rem;
            font-weight: 900;
            color: white;
            letter-spacing: 3px;
        }

        .hero {
            height: 100vh;
            background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.75)), 
                        url('https://source.unsplash.com/random/1920x1080/?potato-chips') center/cover;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .chips-bg {
            position: absolute;
            inset: 0;
            background: url('https://source.unsplash.com/random/600x600/?potato-chips') repeat;
            opacity: 0.18;
            animation: chipsMove 22s linear infinite;
        }

        @keyframes chipsMove {
            0% { background-position: 0
