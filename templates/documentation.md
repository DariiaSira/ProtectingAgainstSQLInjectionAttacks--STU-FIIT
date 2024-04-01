## HTML Templates Documentation

### search_users.html
1. This HTML template represents the user search form.
2. It contains a form where users can enter a username to search for.
3. The form uses the POST method to submit the search query.
4. A CSRF token is included for security.
5. The input field has the name "search_query" and a placeholder text "Enter username".
6. A submit button allows users to initiate the search.

### search_results.html
1. This HTML template displays the search results.
2. It shows a header with the title "Search Results".
3. Inside an unordered list (ul), it iterates over each user in the 'users' context variable.
4. For each user, it checks if the 'id' attribute exists.
   * If the 'id' attribute exists, it displays the user's id, username, email, and password.
   * If the 'id' attribute doesn't exist, it assumes that the user object is returned as a tuple and displays its elements accordingly.
5. If no users are found (the 'users' variable is empty), it displays a message "No users found" within a list item (li).
6. This template is used to render the search results returned by both the vulnerable and protected search views.


### Additional explanation
### Combining Different Data Formats in Django Templates

When developing web applications in Django, there may be a need to display data obtained from different sources in the same template. For example, when using a mixed approach, where some data is obtained through Django's ORM (model objects) and others through direct SQL queries (data tuples).

In such situations, it is important to consider the difference in data structure between Django model objects and data tuples. Django model objects typically have attributes (such as id, username, email, password), whereas data tuples obtained directly through SQL queries may contain fields as indices (e.g., 0, 1, 2, 3).

To successfully combine different data formats in a template, it is recommended to use a conditional expression {% if %} to correctly choose the output format based on the data type. For example:

```
{% for user in users %}
    {% if user.id %}
        <!-- Use Django model objects -->
        <li>{{ user.id }}: {{ user.username }} - {{ user.email }} - {{ user.password }}</li>
    {% else %}
        <!-- Use data tuples -->
        <li>{{ user.0 }}: {{ user.1 }} - {{ user.2 }} - {{ user.3 }}</li>
    {% endif %}
{% empty %}
    <li>No users found</li>
{% endfor %}
```


In this example, the condition {% if user.id %} checks for the existence of the id attribute in the user variable. If the id attribute exists (i.e., user is a Django model object), the output format for model objects is used. Otherwise (if user is a data tuple), the output format for data tuples is used.

This approach allows for efficient management of different data formats and provides flexibility in developing templates in Django.