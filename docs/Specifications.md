# Specifications
## 1. Mobile App
We separate the features of the app in various tasks:
- Account
- Data reporting
- Visualisation
- Exchange center
- Language
- On and Offline

### 1.1. Account
The user should be able to sign in to his account. Anonymous data contributions should not be permitted since this can encourage data spamming. Data should be traceable.
Login can be done with auth providers (Google, or maybe facebook) or by a custom email/password with account verification.

The user should be able to delete his account in the app.

### 1.2. Data reporting
Reporting is done by filling a form and providing a proof (photo or 30 seconds max video length with max 16Mb data). 
Reporting consist of description, location and proof. Relevant permissions must then be taken since incidents reported are to be geolocated.

Data reporting should be done either on:
#### 1.2.1. Road infrastructure
Here the user reports the road infrastructure state, the description form should follow these requirements

#### 1.2.2. Road accidents
Here the user reports accidents (do not provide victimes photos or videos).

### 1.3. Visualization
Data visualization is done by:
#### 1.3.1.Charts
The user can visualize the data on charts. The data presented on charts are preprocessed by the backend of the solution.
Filtering and other tools should permit the user to better appreciate the data.

#### 1.3.2. Maps
The data interpreted can be displayed on maps, visualize zones on interest.

### 1.4. Exchange center
This can be an open space where the user can express themselves for the different aspects (maybe suggestions). Attention should be made, since this part requires content moderation, surveillance and action. It can be discarded if not needed.

## 2. Website
The main features on the website goes to making the data accessible and open:
- Account
- Visualization
- Exchange center

### 2.1. Account
Here, sign in is not a requirement as all feature can be accessed (except the exchange center). Login can be done with auth providers (Google, or maybe facebook) or by a custom email/password with account verification.

### 2.2. Visualization
Further visualization compared to the mobile app should be possible, both on map and charts.

We need to define any road safety formulae checks we are using.

### 2.3. Exchange center
Here the exchange center should have more features:
#### Download
The user should be able to download the data of interest (or the part filtered in data visualization). The data should be in .csv or excel file to enable further treatment.

#### 2.4. Articles and blogs
The user should have access to the articles, blogs and latest news related to road safety and initiatives.

## 3. Language
The app and website should be multilingual. Additional languages can be added with due time. We first aim for french and english

## 3. On and Offline
The user can use the app with and without internet. Offline mode should permit cloud sync when connected to the internet. The data should be persisted between usage.
Offline mode will not be the case of the website.