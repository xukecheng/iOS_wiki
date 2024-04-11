##  Phantom types in Swift

18 Feb 2021

Not every language with a static type system has so strong type-safety like
Swift. Swift features like phantom types, generic type extensions, enums with
associated types create an excellent foundation. This week we will learn how
to use phantom types to build type-safe APIs.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

A phantom type is a generic type that is declared but never used inside a type
where it is declared. It is usually used as a generic constraint to build a
more type-safe and robust API. Let’s take a look at the quick example.

    
    
    struct Identifier<Holder> {
        let value: Int
    }
    

In the example above, we have the _Identifier_ struct with a generic _Holder_
type declared. As you can see, we don’t use the _Holder_ type inside the
_Identifier_ type. That’s why it is called phantom type. Now let’s think about
the benefits of using phantom types like this.

    
    
    struct User {
        let id: Identifier<Self>
    }
    
    struct Product {
        let id: Identifier<Self>
    }
    
    let product = Product(id: .init(value: 1))
    let user = User(id: .init(value: 1))
    
    user.id == product.id
    

We create _User_ and _Product_ types and use the previously created
_Identifier_ struct. We set the value of the identifier to 1 for the newly
created user and product. But when we try to compare them, the Swift compiler
fails with the error:

> Binary operator ‘==’ cannot be applied to operands of type ‘ _Identifier-
> User_ ’ and ‘ _Identifier-Product_ ’.

And that’s great because there is no reason to compare user and product
identifiers. We can do it only accidentally. The Swift compiler doesn’t allow
us to mix the identifiers between users and products because of phantom type
and recognize them as entirely different types. Here is another example where
the Swift compiler doesn’t allow us to mix identifiers.

    
    
    func fetch(_ product: Identifier<Product>) -> Product? {
        // return product by id
    }
    
    fetch(user.id)
    

> To learn more about the benefits of using phantom types, look at my [
> “Building type-safe networking in Swift” ](/2021/02/10/building-type-safe-
> networking-in-swift/) post.

####  Type safety in HealthKit

We learned the basics of phantom types. Now we can move to more advanced
examples. I built a couple of health-oriented apps that use HealthKit to store
and query health data from the Apple Watch. Let’s look at the typical code
that I use to fetch data from the Apple Health app.

    
    
    import HealthKit
    
    let store = HKHealthStore()
    let bodyMass = HKQuantityType.quantityType(
        forIdentifier: HKQuantityTypeIdentifier.bodyMass
    )!
    let query = HKStatisticsQuery(
        quantityType: bodyMass,
        quantitySamplePredicate: nil,
        options: .discreteAverage
    ) { _, statistics, _ in
        let average = statistics?.averageQuantity()
        let mass = average?.doubleValue(for: .meter())
    }
    
    store.execute(query)
    

In the example above, we create a query to fetch user’s weight from the Apple
Health app. In the completion handler, we try to get the average and convert
it to meters. As you can guess, it is impossible to convert body mass to
meters, and the app will crash here. We will try to solve the issue by
introducing phantom type to build more type-safe API.

    
    
    enum Distance {
        case mile
        case meter
    }
    
    enum Mass {
        case pound
        case gram
        case ounce
    }
    
    struct Statistics<Unit> {
        let value: Double
    }
    
    
    extension Statistics where Unit == Mass {
        func convert(to unit: Mass) -> Double {
    
        }
    }
    
    extension Statistics where Unit == Distance {
        func convert(to unit: Distance) -> Double {
    
        }
    }
    
    let weight = Statistics<Mass>(value: 75)
    weight.convert(to: Distance.meter)
    

Here is a possible solution for the HealthKit framework that uses phantom type
to improve API safety. We introduce _Mass_ and _Distance_ enums to have
distinct units. And as soon you try to convert mass into the distance, the
Swift compiler stops you with a great error message:

> Cannot convert the value of type ‘ _Distance_ ’ to expected argument type ‘
> _Mass_ ’

####  Conclusion

Today we learned phantom types, one of my favorite features of the Swift
language. It looks like there are a lot of possible applications for phantom
types. Feel free to share with me how you make your API more type-safe by
using phantom types. I hope you enjoy the post. Follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this article.
Thanks for reading, and see you next week!

