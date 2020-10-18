
#include <stdio.h>
#include <string.h>


struct Product
{
    char* name;
    double price;
};

struct ProductStock
{
    struct Product product;
    int quantity;
};

struct Shop
{
    double cash;
    struct ProductStock stock[20];
};

struct Customer
{
    char* name;
    double budget;
    struct ProductStock shoppingList[10];

};


void printProduct(struct Product p)
{
    printf("---------------------------------------\n");
    printf("Product name: %s \nProduct price: %.2f Euro\n", p.name, p.price);
    printf("---------------------------------------\n");
}

void printCustomer(struct Customer c)
{
    printf("---------------------------------------\n");
    printf("Customer name: %s \nCustomer budget: %.2f Euro\n", c.name, c.budget);
    printf("---------------------------------------\n");
}


int main(void)
{
    struct Product coke = { "Can of coke", 1.05};
    printProduct(coke);

    struct Customer karolina = { "Karolina", 100.00, "Euro"};
    printCustomer(karolina);

    struct ProductStock cokeStock = {coke, 120};
    printf("The shop has %d of the product, which are: %s\n", cokeStock.quantity, cokeStock.product.name);
    
    return 0;


}