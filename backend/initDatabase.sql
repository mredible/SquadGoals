create table Users(
UserID int primary key auto_increment,
username char(20) not null,
description text,
password char(20) not null,
Unique(username)
 );

insert into Users(username, description, password) values (
'Bethany', 'Amateur coder, passionate about dancing and watersports', 'suema76s');

insert into Users(username, password) values ("Brittame", "ga4i29c");

create table Squads(
SquadID int primary key auto_increment,
name char(20) not null,
description text,
pictureURL text,
dateCreated date
);

insert into Squads(name, description) values
("Guitar", "Community to bring Guitar enthusiasts together"),
("Learn French", "Community to help people practice their French speaking");

create table Goals(
GoalID int primary key auto_increment,
name char(50) not null,
description text,
dateCreated date
);

insert into Goals(name, description) values
("Go for walks", "Reach 10,000 steps a day"),
("Read bible", "Listen to bible podcast once a day"),
("Improve French", "Do duolingo and read french news articles");


create table Users_Squads(
userID int not null,
squadID int not null,
foreign key (userID) references Users(UserID),
foreign key (squadID) references Squads(SquadID)
);

insert into Users_Squads(userID, squadID) values (1, 2), (2,1), (2,2);

/*select u.UserID, us.userID, s.SquadID, us.squadID, u.username, s.name, s.description from Users_Squads us, Squads s, Users u where u.UserID=us.userID and s.SquadID=us.squadID;*/

create table Squads_Goals(
goalID int not null,
squadID int not null,
foreign key (goalID) references Goals(GoalID),
foreign key (squadID) references Squads(SquadID)
);

insert into Squads_Goals(goalID, squadID) values (3, 2);

create table Users_Goals(
goalID int not null,
userID int not null,
foreign key (goalID) references Goals(GoalID),
foreign key (userID) references Users(UserID)
);

insert into Users_Goals(goalID, userID) values (1,1), (2,1), (1,2), (3,2);

create table Friends(
userID1 int not null,
userID2 int not null,
friendshipDate date,
foreign key (userID1) references Users(UserID),
foreign key (userID2) references Users(UserID)
);

insert into Friends(userID1, userID2) values (1,2);

create table Goal_Updates(
UpdateID int primary key auto_increment,
goalID int not null,
description text,
updateDate date,
foreign key (goalID) references Goals(GoalID)
);

insert into Goal_Updates(goalID, description) values
(1,"Walk a mile a day"), (3, "Meet up with french speaking people");
