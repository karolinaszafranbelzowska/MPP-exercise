
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


int main()
{
    struct Product coke = { "Can of coke", 1.05};
    printf("The %s costs %.2f Euro\n", coke.name, coke.price);

    struct Customer karolina = { "Karolina", 100.00, "Euro"};
    printf("Customer name is %s\n", karolina.name);

    struct ProductStock cokeStock = {coke, 120};
    printf("The shop has %d of the product, which are: %s\n", cokeStock.quantity, cokeStock.product.name);
    
    return 0;


}