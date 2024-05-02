## System Documentation

The Rheoli Cyfoeth is a simple storage manager for a company, but is useful for a home, church or a NGO. 
There are 3 main entities: Users (who control the system), Departments (or sectors, where the items are stored) and Items (chairs, tables, computers, etc...)
It's pretty simple but it's resolves the problem. It may grow easily too.

#### Users
- Only Create a new user and login shouldn't require being authenticated, every other endpoint should require authentication
- Get endpoints must have 2 rules:
    - If user is admin (is_staff == True), it has access to all users details (Get by id/username) and get all users
    - If user is not admin, it has access only to its user data
        - In the future, this rule may change to only get few data from the other user (like name and if it's admin)
- Update and Delete endpoints should validate if the user is admin

### Departments
- Create or Delete endpoints should validate if the user is admin
- When creating or updating endpoints, it shouldn't be necessary receive an object for the manager, only the ManagerId is required
- When retrieving all departments or only one department, the departments objects should contains the manager data
- The system should be able to retrieve all items from an department

### Movings History
- Only requires authentication
- Should only have the create moving history endpoint. The moving data should be retrieved from the Item object
- The Moving History should have an existent destination department, an existent initial department and an existent Item
- The Moving History should not have a finish date equals than other moving history from the same item.

### Item
- When creating or updating an Item, it shouldn't be necessary receive an department object, only the department id is required
- All endpoints should be public for a authenticated user