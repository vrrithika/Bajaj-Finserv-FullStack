# Bajaj-Finserv-FullStack
# Bajaj Finserv REST API Challenge

This project is a **FastAPI-based REST API** that processes an input array and returns structured information such as numbers, alphabets, special characters, and transformations.

---

## 🚀 Features

The API accepts a **POST request** with an array and returns:

1. **Status** – Success/Failure  
2. **User ID**  
3. **Email ID**  
4. **College Roll Number**  
5. **Even Numbers** – Extracted from the array  
6. **Odd Numbers** – Extracted from the array  
7. **Alphabets (Uppercase)** – All alphabets converted to uppercase  
8. **Special Characters** – Non-alphanumeric characters extracted  
9. **Sum of Numbers** – Sum of all integers in the array  
10. **Concatenation of Alphabets (Reversed Alternating Caps)** – Alphabets concatenated in reverse order with alternating capitalization  

---

## 📌 Example Request

```http
POST /bfhl
Content-Type: application/json

