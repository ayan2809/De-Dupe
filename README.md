# De-Dupe
De-duplication Engine for NOSQL database

# De-Dupe Engine

Our project is regarding the de duplication check for deduplication
with an existing database.

### Setbacks with Duplicate Data

- Presence of duplicate entries can be a huge problem when seen from a storage perspective. Storage isn't cheap. Hence there is a need to minimize storage by avoiding these duplicates.

- With the presence of duplicate data, larger is the dataset/database. This is seen as a hindrance for any searching/sorting algorithm as their efficiency is inversely proportional to the size of the data.

### How do we overcome this?

Deduplication Engine is an approach towards solving this problem.
Deduplication is a technique that minimizes the
amount of space required to save data on a given storage medium. As
the name suggests, it is designed to combat the problem
organizations of all sizes deal with on a regular basis – duplicate data.
For some, it’s an accumulation of the exact same files. For others, it’s
a collection of files that aren’t completely identical yet contain pieces
of the same data

## Features

- A Single Data comparision
- Bulk Data Comparision
- Fine Tuning the weights for data columns
- Sharding of Data in the Database level
- Multi Threading to optimize our approach

## Tech Stack

Frontend: HTML, CSS, JS, Jquery

Server: Flask

API: Rest API

Backend: Flask

Hosting: Heroku

Hosted App 
https://de-dupe.herokuapp.com/

Project Demo 
https://drive.google.com/file/d/1rHocUQV9PsF3xtH69zrT00yKpPLM9VYG/view?usp=sharing
