from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from project.api.auth.views import GetFeedView, UsersListView


app_name = 'api'

urlpatterns = [
    path('feed/', GetFeedView.as_view(), name='feed'),
    path('users/', UsersListView.as_view(), name='users_list'),
    # path('feed/<int:user_id>/', GetUserView.as_view(), name='users_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# /api/feed/ GET: lists all the posts of all users in chronological order
# /api/feed/<int:user_id>/ GET: lists all the posts of a specific user in chronological order
# /api/feed/followers/ GET: lists all the posts of followed users in chronological order
# /api/posts/<int:post_id>/ GET: get a specific post by ID and display all the information
# /api/posts/<int:post_id>/ POST: update a specific post (only by owner of post or admin)
# /api/posts/<int:post_id>/ DELETE: delete a post by ID (only by owner of post or admin)
# /api/posts/new-post/ POST: user can make a new post by sending post data
# /api/posts/likes/ GET: the list of the posts the user like
# /api/posts/like/<int:post_id>/ POST: like a post
# /api/users/followers/ GET: List of all the followers
# /api/users/following/ GET: List of all the people the user is following
# /api/users/follow/<int:user_id>/ POST: follow a user
# /api/users/unfollow/<int:user_id>/ POST: unfollow a user

# /api/auth/token/ POST: Get a new JWT by passing username and password
# /api/auth/token/refresh/ POST: Get a new JWT by passing an old still valid JWT.
# /api/feed/?search=<str:search_string> GET: Search posts of all users and list result in chronological order
# /api/posts/<int:post_id>/dislike/ POST: dislike a post
# /api/posts/share-post/<int:post_id> POST: User can share a post they like from another user
# (this creates a new post on this user with no content but a share relation)
# /api/me/ GET: Get my user profile (as well private information like email, etc.)
# /api/me/ POST: Update my user profile
# /api/users/ GET: Get all the users
# /api/users/?search=<str:search_string> GET: Search users
# /api/users/<int:user_id>/ GET: Get specific user profile (only public infos)
# /api/registration/ POST: Register a new user by asking for an email (send email validation code)
# /api/registration/validation/ POST: Validate a new registered user with validation code sent by email
# /api/users/friendrequests/ GET: List all open friend requests from others
# /api/users/friendrequests/<int:user_id>/ POST: Send friendrequest to user
# /api/users/friendrequests/pending/ GET: List all my pending friend requests
# /api/users/friendrequests/accept/<int:request_id>/ POST: Accept a open friend request
# /api/users/friendrequests/reject/<int:request_id>/ POST: Reject a open friend request
# /api/users/friends/ GET: List all friends
# /api/users/friends/unfriend/ POST: Unfriend a friend
# /api/feed/friends/ GET: lists all the posts of my friends in chronological order
# /api/auth/password-reset/ POST: Reset users password by sending a validation code in a email
# /api/auth/password-reset/validate/ POST: Validate password reset token and set new password for the user
