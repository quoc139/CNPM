"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CNPM_DAU</title>
        <style>
            body {
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                background: linear-gradient(135deg, #e0f7fa, #f3e5f5);
                font-family: Arial, sans-serif;
            }
            .card {
                background: white;
                padding: 40px 60px;
                border-radius: 18px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
                text-align: center;
                display: flex;
                align-items: center;
                gap: 28px;
            }
            .logo-wrap {
                width: 150px;
                height: 150px;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
                background: #f7fbff;
                border-radius: 16px;
                padding: 8px;
                border: 2px solid #dfeeff;
            }
            .logo-wrap img {
                width: 100%;
                height: 100%;
                object-fit: contain;
                display: block;
            }
            .text-box {
                text-align: left;
            }
            h1 {
                color: #1e88e5;
                margin-bottom: 12px;
            }
            p {
                color: #333;
                font-size: 22px;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="logo-wrap" aria-label="Logo trường Đại học Kiến Trúc Đà Nẵng">
                <img
                    src="https://media.dau.edu.vn/Media/1_TH1057/Images/logo-dhktdn-copy.png"
                    alt="Logo Đại học Kiến Trúc Đà Nẵng"
                    title="Đại học Kiến Trúc Đà Nẵng"
                >
            </div>
            <div class="text-box">
                <h1>Chào bạn khóa 24CT</h1>
                <p>đến với học phần <strong>CNPM_DAU</strong></p>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
