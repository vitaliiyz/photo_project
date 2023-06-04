from django.shortcuts import render

head_imgs = ["images/slide1.jpg", "images/slide2.jpg", "images/slide3.jpg"]

GALLERIES = [
    {
        "title": "Lovely Smiles_1",
        "tag_1": "Design_1",
        "tag_2": "Illustrations_1",
        "image_1": "images/11.jpg",
        "image_2": "images/1.jpg",
    },
    {
        "title": "Lovely Smiles_2",
        "tag_1": "Design_2",
        "tag_2": "Illustrations_2",
        "image_1": "images/6.jpg",
        "image_2": "images/8.jpg",
    },
    {
        "title": "Lovely Smiles_3",
        "tag_1": "Design_3",
        "tag_2": "Illustrations_3",
        "image_1": "images/14.jpg",
        "image_2": "images/3.jpg",
    },
    {
        "title": "Lovely Smiles_4",
        "tag_1": "Design_4",
        "tag_2": "Illustrations_4",
        "image_1": "images/5.jpg",
        "image_2": "images/4.jpg",
    },
    {
        "title": "Lovely Smiles_5",
        "tag_1": "Design_5",
        "tag_2": "Illustrations_5",
        "image_1": "images/2.jpg",
        "image_2": "images/12.jpg",
    },
    {
        "title": "Lovely Smiles_6",
        "tag_1": "Design_6",
        "tag_2": "Illustrations_6",
        "image_1": "images/9.jpg",
        "image_2": "images/7.jpg",
    },
]


def home_page(request):
    return render(request, "home.html", {"carousel": head_imgs, "galleries": GALLERIES})
