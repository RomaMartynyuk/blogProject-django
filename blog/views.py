from datetime import date

from django.shortcuts import render

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountain.jpg',
        'author': 'Roman',
        'date': date(2023, 11, 20),
        'title': 'Mountain Hiking',
        'excerpt': 'There\'s nothing like the views you get when hiking in the mountains!',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.
        """
    },
    {
        'slug': 'racing-cars',
        'image': 'racing.jpg',
        'author': 'Roman',
        'date': date(2024, 6, 5),
        'title': 'Car Racing',
        'excerpt': 'There\'s nothing better than adrenaline while you race the one of fastest cars in history!',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.
        """
    },
    {
        'slug': 'gym-exercises',
        'image': 'gym.jpg',
        'author': 'Roman',
        'date': date(2007, 12, 29),
        'title': 'Gym Exercises',
        'excerpt': 'There\'s nothing better than lift bigger weight from one to next train, bigger, bigger and bigger!',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus vitae ante ac dolor suscipit vehicula eget ut dui.
            Vestibulum ac lobortis massa, ac malesuada dolor. Ut diam sem,
            convallis pulvinar molestie vel, ullamcorper eu libero. Etiam ac maximus sem,
            sit amet consectetur felis. Mauris malesuada dignissim justo,
            eget efficitur augue feugiat a. Nam accumsan lorem mi,
            quis ornare lectus scelerisque sit amet. Morbi sit amet varius sapien.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
