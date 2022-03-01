USE ymca
GO

DROP TABLE dbo.History;
DROP TABLE dbo.Program;
DROP TABLE dbo.[User];

CREATE TABLE [User](
	FNAME nvarchar(20) NOT NULL,
	LNAME nvarchar(20) NOT NULL,
	DOB date NOT NULL,
	EMAIL nvarchar(20) NOT NULL,
	[PASSWORD] nvarchar(20) NOT NULL,
	[TYPE] nvarchar(1) NOT NULL,
	USERID int IDENTITY(1,1) PRIMARY KEY 
);

CREATE TABLE Program(
	PROGRAMID int IDENTITY(1,1) PRIMARY KEY,
	[DESCRIPTION] nvarchar(max),
	[NAME] nvarchar(20) NOT NULL,
	LOCATION nvarchar(20) NOT NULL,
	FEE int NOT NULL,
	[TIME] time NOT NULL,
	STARTDATE date NOT NULL,
	ENDDATE date NOT NULL,
	[LENGTH] int NOT NULL,
	[DAY] int NOT NULL,
	SIZE int NOT NULL,
	USERID int,
	FOREIGN KEY (USERID) REFERENCES dbo.[User](USERID) 
);

CREATE TABLE History(
	USERID int,
	PROGRAMID int,
	[STATUS] nvarchar(1) NOT NULL,
	FOREIGN KEY (USERID) REFERENCES dbo.[User](USERID),
	FOREIGN KEY (PROGRAMID) REFERENCES dbo.Program(PROGRAMID)
);

INSERT INTO dbo.[User] (FNAME, LNAME, DOB, EMAIL, [PASSWORD], [type])
VALUES ('admin', 'admin', '1/1/1900', 'admin', 'admin', 'S'),
VALUES ('Jane', 'Doe', '1/1/1967', 'jdoe@gmail.com', 'jdoe', 'M'),
VALUES ('Luke', 'Anderson', '10/15/1975', 'landerson@gmail.com', 'landerson', 'N')


INSERT INTO dbo.Program ([DESCRIPTION], [NAME], LOCATION, FEE, [TIME], STARTDATE, ENDDATE, [LENGTH], [DAY], SIZE, USERID)
VALUES ('introduction to rock climbing', 'Rockclimbing 1', 'Onalaska', 100, '4:00', '3/22/22', '4/22/22', 90, 2, 30, 1),
('intermediate rock climbing', 'Rockclimbing 2', 'Onalaska', 100, '4:00', '3/22/22', '4/22/22', 90, 2, 30, 1),
('advanced rock climbing', 'Rockclimbing 3', 'Onalaska', 100, '4:00', '3/22/22', '4/22/22', 90, 2, 30, 1)