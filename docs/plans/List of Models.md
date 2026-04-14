**List of Models**

User:

- This will be for account registration, auth, login/logout
- Will use built-in Django User model

- primary fields:
  - id PK
  - username
  - email
  - password
  - 1:1 User:Profile

Profile:

- for specific info about users

- primary fields:
  - id PK
  - user FK(OneToOneField??)
  - profile_image(optional)
  - display_name
  - bio(optional)
  - link(optional)
  - created
  - last_updated
  - 1:1 User:Profile
  - 1:M Profile:Flyer

Flyer:

- stores actual flyer
- will have a default font, sizes, and layout.

- fields:
  - id PK
  - profile FK
  - event_name
  - event_date
  - event_location
  - cover_charge
  - link (optional)
  - image(optional)
  - bg_color
  - font_color
  - font_family
  - flyer_name
  - created
  - last_updated
  - M:1 Flyer:Profile
  - 1:M Profile:Flyer

Flyer only edited or deleted by the user who owns that profile attached to that flyer.
