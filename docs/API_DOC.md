---
title: Online store API v1
<h1 id="online-store-api">Online store API v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="online-store-api-comment">comment</h1>

Operations for comments.

## Create new comment

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/comment', headers = headers)

print(r.json())

```

`POST /comment`

> Body parameter

```json
{
  "product_id": 0,
  "content": "string"
}
```

<h3 id="post__comment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Comment](#schemacomment)|true|none|

> Example responses

> 422 Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__comment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="online-store-api-product">product</h1>

Operations for product.

## Get product by ID

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/product/{product_id}', headers = headers)

print(r.json())

```

`GET /product/{product_id}`

<h3 id="get__product_{product_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "name": "string",
  "id": 0,
  "price": 0,
  "comments": [
    {
      "user": {
        "name": "string"
      },
      "content": "string",
      "id": 0
    }
  ],
  "description": "string"
}
```

<h3 id="get__product_{product_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Product](#schemaproduct)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Update product info with ID (Admin login required)

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/product/{product_id}', headers = headers)

print(r.json())

```

`PUT /product/{product_id}`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "price": 0
}
```

<h3 id="put__product_{product_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProductUpdate](#schemaproductupdate)|true|none|
|product_id|path|integer|true|none|

> Example responses

> 201 Response

```json
{
  "description": "string",
  "name": "string",
  "id": 0,
  "price": 0
}
```

<h3 id="put__product_{product_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Product1](#schemaproduct1)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Delete a product by ID (Admin login required)

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/product/{product_id}', headers = headers)

print(r.json())

```

`DELETE /product/{product_id}`

<h3 id="delete__product_{product_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

> default Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="delete__product_{product_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Search for products

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.get('/product', headers = headers)

print(r.json())

```

`GET /product`

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="get__product-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProductSearch](#schemaproductsearch)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "name": "string",
    "id": 0,
    "price": 0,
    "comments": [
      {
        "user": {
          "name": "string"
        },
        "content": "string",
        "id": 0
      }
    ],
    "description": "string"
  }
]
```

<h3 id="get__product-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<h3 id="get__product-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Product](#schemaproduct)]|false|none|none|
|» name|string|true|none|none|
|» id|integer|false|read-only|none|
|» price|number|true|none|none|
|» comments|[[Comment1](#schemacomment1)]|false|read-only|none|
|»» user|[BaseUser](#schemabaseuser)|false|read-only|none|
|»»» name|string|true|none|none|
|»» content|string|true|none|none|
|»» id|integer|false|read-only|none|
|»» product_id|integer|true|write-only|none|
|» description|string|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Create a new product (Admin login required)

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/product', headers = headers)

print(r.json())

```

`POST /product`

> Body parameter

```json
{
  "name": "string",
  "price": 0,
  "description": "string"
}
```

<h3 id="post__product-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Product](#schemaproduct)|true|none|

> Example responses

> 200 Response

```json
{
  "description": "string",
  "name": "string",
  "id": 0,
  "price": 0
}
```

<h3 id="post__product-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[BaseProduct](#schemabaseproduct)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Get all comments for product

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/product/{product_id}/comments', headers = headers)

print(r.json())

```

`GET /product/{product_id}/comments`

<h3 id="get__product_{product_id}_comments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

> 200 Response

```json
[
  {
    "user": {
      "name": "string"
    },
    "content": "string",
    "id": 0
  }
]
```

<h3 id="get__product_{product_id}_comments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|default|Default|Default error response|[Error](#schemaerror)|

<h3 id="get__product_{product_id}_comments-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Comment1](#schemacomment1)]|false|none|none|
|» user|[BaseUser](#schemabaseuser)|false|read-only|none|
|»» name|string|true|none|none|
|» content|string|true|none|none|
|» id|integer|false|read-only|none|
|» product_id|integer|true|write-only|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="online-store-api-auth">auth</h1>

Operations for authentication.

## Register a new user

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/register', headers = headers)

print(r.json())

```

`POST /register`

> Body parameter

```json
{
  "role": "admin",
  "password": "string",
  "email": "user@example.com",
  "name": "string"
}
```

<h3 id="post__register-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[User](#schemauser)|true|none|

> Example responses

> 422 Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__register-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Update user info (Login required)

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/user', headers = headers)

print(r.json())

```

`PUT /user`

> Body parameter

```json
{
  "email": "user@example.com",
  "role": "admin",
  "name": "string"
}
```

<h3 id="put__user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserUpdate](#schemauserupdate)|true|none|

> Example responses

> 422 Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="put__user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Login

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/login', headers = headers)

print(r.json())

```

`POST /login`

> Body parameter

```json
{
  "email": "user@example.com",
  "password": "string"
}
```

<h3 id="post__login-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserLogin](#schemauserlogin)|true|none|

> Example responses

> 422 Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Logout (Login required)

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/logout', headers = headers)

print(r.json())

```

`POST /logout`

> Example responses

> default Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__logout-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Reset password

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/reset-password', headers = headers)

print(r.json())

```

`POST /reset-password`

> Body parameter

```json
{
  "new_confirm_password": "string",
  "current_password": "string",
  "new_password": "string"
}
```

<h3 id="post__reset-password-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserPasswordUpdate](#schemauserpasswordupdate)|true|none|

> Example responses

> 422 Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__reset-password-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity|[Error](#schemaerror)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Get current user infomation

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/user-info', headers = headers)

print(r.json())

```

`GET /user-info`

> Example responses

> 200 Response

```json
{
  "role": "admin",
  "email": "user@example.com",
  "name": "string",
  "id": 0
}
```

<h3 id="get__user-info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[BaseUser1](#schemabaseuser1)|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Refresh token

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/refresh', headers = headers)

print(r.json())

```

`POST /refresh`

> Example responses

> default Response

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}
```

<h3 id="post__refresh-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|Default error response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Error">Error</h2>
<!-- backwards compatibility -->
<a id="schemaerror"></a>
<a id="schema_Error"></a>
<a id="tocSerror"></a>
<a id="tocserror"></a>

```json
{
  "code": 0,
  "errors": {},
  "message": "string",
  "status": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|Error code|
|errors|object|false|none|Errors|
|message|string|false|none|Error message|
|status|string|false|none|Error name|

<h2 id="tocS_PaginationMetadata">PaginationMetadata</h2>
<!-- backwards compatibility -->
<a id="schemapaginationmetadata"></a>
<a id="schema_PaginationMetadata"></a>
<a id="tocSpaginationmetadata"></a>
<a id="tocspaginationmetadata"></a>

```json
{
  "total": 0,
  "total_pages": 0,
  "first_page": 0,
  "last_page": 0,
  "page": 0,
  "previous_page": 0,
  "next_page": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|false|none|none|
|total_pages|integer|false|none|none|
|first_page|integer|false|none|none|
|last_page|integer|false|none|none|
|page|integer|false|none|none|
|previous_page|integer|false|none|none|
|next_page|integer|false|none|none|

<h2 id="tocS_BaseUser">BaseUser</h2>
<!-- backwards compatibility -->
<a id="schemabaseuser"></a>
<a id="schema_BaseUser"></a>
<a id="tocSbaseuser"></a>
<a id="tocsbaseuser"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|

<h2 id="tocS_BaseProduct">BaseProduct</h2>
<!-- backwards compatibility -->
<a id="schemabaseproduct"></a>
<a id="schema_BaseProduct"></a>
<a id="tocSbaseproduct"></a>
<a id="tocsbaseproduct"></a>

```json
{
  "description": "string",
  "name": "string",
  "id": 0,
  "price": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|true|none|none|
|name|string|true|none|none|
|id|integer|false|read-only|none|
|price|number|true|none|none|

<h2 id="tocS_Comment">Comment</h2>
<!-- backwards compatibility -->
<a id="schemacomment"></a>
<a id="schema_Comment"></a>
<a id="tocScomment"></a>
<a id="tocscomment"></a>

```json
{
  "product_id": 0,
  "id": 0,
  "user": {
    "name": "string"
  },
  "content": "string",
  "product": {
    "description": "string",
    "name": "string",
    "id": 0,
    "price": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|true|write-only|none|
|id|integer|false|read-only|none|
|user|[BaseUser](#schemabaseuser)|false|read-only|none|
|content|string|true|none|none|
|product|[BaseProduct](#schemabaseproduct)|false|read-only|none|

<h2 id="tocS_Comment1">Comment1</h2>
<!-- backwards compatibility -->
<a id="schemacomment1"></a>
<a id="schema_Comment1"></a>
<a id="tocScomment1"></a>
<a id="tocscomment1"></a>

```json
{
  "user": {
    "name": "string"
  },
  "content": "string",
  "id": 0,
  "product_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user|[BaseUser](#schemabaseuser)|false|read-only|none|
|content|string|true|none|none|
|id|integer|false|read-only|none|
|product_id|integer|true|write-only|none|

<h2 id="tocS_Product">Product</h2>
<!-- backwards compatibility -->
<a id="schemaproduct"></a>
<a id="schema_Product"></a>
<a id="tocSproduct"></a>
<a id="tocsproduct"></a>

```json
{
  "name": "string",
  "id": 0,
  "price": 0,
  "comments": [
    {
      "user": {
        "name": "string"
      },
      "content": "string",
      "id": 0,
      "product_id": 0
    }
  ],
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|id|integer|false|read-only|none|
|price|number|true|none|none|
|comments|[[Comment1](#schemacomment1)]|false|read-only|none|
|description|string|true|none|none|

<h2 id="tocS_ProductUpdate">ProductUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaproductupdate"></a>
<a id="schema_ProductUpdate"></a>
<a id="tocSproductupdate"></a>
<a id="tocsproductupdate"></a>

```json
{
  "name": "string",
  "description": "string",
  "price": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|description|string|false|none|none|
|price|number|false|none|none|

<h2 id="tocS_Product1">Product1</h2>
<!-- backwards compatibility -->
<a id="schemaproduct1"></a>
<a id="schema_Product1"></a>
<a id="tocSproduct1"></a>
<a id="tocsproduct1"></a>

```json
{
  "description": "string",
  "name": "string",
  "id": 0,
  "price": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|true|none|none|
|name|string|true|none|none|
|id|integer|false|read-only|none|
|price|number|true|none|none|

<h2 id="tocS_ProductSearch">ProductSearch</h2>
<!-- backwards compatibility -->
<a id="schemaproductsearch"></a>
<a id="schema_ProductSearch"></a>
<a id="tocSproductsearch"></a>
<a id="tocsproductsearch"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "role": "admin",
  "password": "string",
  "email": "user@example.com",
  "name": "string",
  "id": 0,
  "comments": [
    {
      "product_id": 0,
      "id": 0,
      "user": {
        "name": "string"
      },
      "content": "string",
      "product": {
        "description": "string",
        "name": "string",
        "id": 0,
        "price": 0
      }
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|role|string|false|none|none|
|password|string|true|write-only|none|
|email|string(email)|true|none|none|
|name|string|true|none|none|
|id|integer|false|read-only|none|
|comments|[[Comment](#schemacomment)]|false|read-only|none|

#### Enumerated Values

|Property|Value|
|---|---|
|role|admin|
|role|user|

<h2 id="tocS_UserUpdate">UserUpdate</h2>
<!-- backwards compatibility -->
<a id="schemauserupdate"></a>
<a id="schema_UserUpdate"></a>
<a id="tocSuserupdate"></a>
<a id="tocsuserupdate"></a>

```json
{
  "email": "user@example.com",
  "role": "admin",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string(email)|false|none|none|
|role|string|false|none|none|
|name|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|role|admin|
|role|user|

<h2 id="tocS_UserLogin">UserLogin</h2>
<!-- backwards compatibility -->
<a id="schemauserlogin"></a>
<a id="schema_UserLogin"></a>
<a id="tocSuserlogin"></a>
<a id="tocsuserlogin"></a>

```json
{
  "email": "user@example.com",
  "password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string(email)|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_UserPasswordUpdate">UserPasswordUpdate</h2>
<!-- backwards compatibility -->
<a id="schemauserpasswordupdate"></a>
<a id="schema_UserPasswordUpdate"></a>
<a id="tocSuserpasswordupdate"></a>
<a id="tocsuserpasswordupdate"></a>

```json
{
  "new_confirm_password": "string",
  "current_password": "string",
  "new_password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|new_confirm_password|string|true|none|none|
|current_password|string|true|none|none|
|new_password|string|true|none|none|

<h2 id="tocS_BaseUser1">BaseUser1</h2>
<!-- backwards compatibility -->
<a id="schemabaseuser1"></a>
<a id="schema_BaseUser1"></a>
<a id="tocSbaseuser1"></a>
<a id="tocsbaseuser1"></a>

```json
{
  "role": "admin",
  "password": "string",
  "email": "user@example.com",
  "name": "string",
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|role|string|false|none|none|
|password|string|true|write-only|none|
|email|string(email)|true|none|none|
|name|string|true|none|none|
|id|integer|false|read-only|none|

#### Enumerated Values

|Property|Value|
|---|---|
|role|admin|
|role|user|

