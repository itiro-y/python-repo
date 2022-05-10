# Mermaid Tutorial
## Class diagrams

```mermaid
classDiagram
    class Order {
        +OrderStatus status
    }
    class OrderStatus {
        <<enumumeraton>>
        FAILED
        PENDING
        PAID
    }
    class PaymentProcessor {
        <<interface>>
        -String apiKey
        #connect(String url, JSON header)
        +processPayment(Order order) OrderStatus
    }
    class Customer {
        +String name
    }
    Customer <|-- PrivateCustomer
    Customer <|-- BusinessCustomer
    PaymentProcessor <|-- StripePaymentProcessor
    PaymentProcessor <|-- PaypalPaymentProcessor
    Order o-- Customer
    Car *-- Engine 
```
- Symbols for access settings
    - "-" means it's private
    - "#" means it's protected
    - "+" means it's public

<br>

- Relationships
    - Inheritance "<|--"
    - Association
        - Composition "*--"
            - The child exists because it's dependent of its parent
        - Aggregation "o--"
            - The child can exist independently from its parent