class OrderDependency {
    Order order;
    Order dependent;
    public OrderDependency(Order order, Order dependent)
    {
        this.order = order;
        this.dependent = dependent;
    }
}
