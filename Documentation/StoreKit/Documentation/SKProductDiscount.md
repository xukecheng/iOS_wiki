Instance Property

# identifier

A string used to uniquely identify a discount offer for a product.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var identifier: String? { get }

## Discussion

You set up offers and their identifiers in App Store Connect.

## See Also

### Identifying the Discount

`var type: SKProductDiscount.`Type``

The type of discount offer.

`enum SKProductDiscount.Type`

Values representing the types of discount offers an app can present.

Instance Property

# type

The type of discount offer.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var type: SKProductDiscount.`Type` { get }

## See Also

### Identifying the Discount

`var identifier: String?`

A string used to uniquely identify a discount offer for a product.

`enum SKProductDiscount.Type`

Values representing the types of discount offers an app can present.

Instance Property

# price

The discount price of the product in the local currency.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var price: NSDecimalNumber { get }

## Discussion

Use the `priceLocale` to format the price.

## See Also

### Getting Price and Payment Mode

`var priceLocale: Locale`

The locale used to format the discount price of the product.

`var paymentMode: SKProductDiscount.PaymentMode`

The payment mode for this product discount.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# priceLocale

The locale used to format the discount price of the product.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var priceLocale: Locale { get }

## Discussion

Use the locale to format the `price`.

## See Also

### Getting Price and Payment Mode

`var price: NSDecimalNumber`

The discount price of the product in the local currency.

`var paymentMode: SKProductDiscount.PaymentMode`

The payment mode for this product discount.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# paymentMode

The payment mode for this product discount.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var paymentMode: SKProductDiscount.PaymentMode { get }

## Discussion

The payment mode indicates how the product discount `price` is charged:

  * One or more times, for `SKProductDiscount.PaymentMode.payAsYouGo` mode

  * Once in advance, for `SKProductDiscount.PaymentMode.payUpFront` mode

  * No initial charge, for `SKProductDiscount.PaymentMode.freeTrial` mode.

Use the payment mode to display an accurate description of the product
discount in your UI. For design guidance, see Human Interface Guidelines > In-
App Purchase.

## See Also

### Getting Price and Payment Mode

`var price: NSDecimalNumber`

The discount price of the product in the local currency.

`var priceLocale: Locale`

The locale used to format the discount price of the product.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# numberOfPeriods

An integer that indicates the number of periods the product discount is
available.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var numberOfPeriods: Int { get }

## Discussion

A product discount may be available for one or more periods. The period,
defined in `subscriptionPeriod`, is a set number of days, weeks, months, or
years.

The total length of time that a product discount is available is calculated by
multiplying the `numberOfPeriods` by the period.

Note that the discount period is independent of the product subscription
period.

## See Also

### Getting the Discount Duration

`var subscriptionPeriod: SKProductSubscriptionPeriod`

An object that defines the period for the product discount.

Instance Property

# subscriptionPeriod

An object that defines the period for the product discount.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var subscriptionPeriod: SKProductSubscriptionPeriod { get }

## Discussion

This object represents the duration of a single subscription period. A period
is described as a number of units, where a unit can be a
`SKProduct.PeriodUnit.day`, `SKProduct.PeriodUnit.month`,
`SKProduct.PeriodUnit.week`, or `SKProduct.PeriodUnit.year`.

To calculate the total amount of time that the discount price is available to
the user, multiply the `subscriptionPeriod` by `numberOfPeriods`.

Note

The subscription period for the discount is independent of the product's
regular subscription period, and does not have to match in units or duration.

## See Also

### Getting the Discount Duration

`var numberOfPeriods: Int`

An integer that indicates the number of periods the product discount is
available.

Instance Property

# identifier

A string used to uniquely identify a discount offer for a product.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var identifier: String? { get }

## Discussion

You set up offers and their identifiers in App Store Connect.

## See Also

### Identifying the Discount

`var type: SKProductDiscount.`Type``

The type of discount offer.

`enum SKProductDiscount.Type`

Values representing the types of discount offers an app can present.

Instance Property

# type

The type of discount offer.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var type: SKProductDiscount.`Type` { get }

## See Also

### Identifying the Discount

`var identifier: String?`

A string used to uniquely identify a discount offer for a product.

`enum SKProductDiscount.Type`

Values representing the types of discount offers an app can present.

Instance Property

# price

The discount price of the product in the local currency.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var price: NSDecimalNumber { get }

## Discussion

Use the `priceLocale` to format the price.

## See Also

### Getting Price and Payment Mode

`var priceLocale: Locale`

The locale used to format the discount price of the product.

`var paymentMode: SKProductDiscount.PaymentMode`

The payment mode for this product discount.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# priceLocale

The locale used to format the discount price of the product.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var priceLocale: Locale { get }

## Discussion

Use the locale to format the `price`.

## See Also

### Getting Price and Payment Mode

`var price: NSDecimalNumber`

The discount price of the product in the local currency.

`var paymentMode: SKProductDiscount.PaymentMode`

The payment mode for this product discount.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# paymentMode

The payment mode for this product discount.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var paymentMode: SKProductDiscount.PaymentMode { get }

## Discussion

The payment mode indicates how the product discount `price` is charged:

  * One or more times, for `SKProductDiscount.PaymentMode.payAsYouGo` mode

  * Once in advance, for `SKProductDiscount.PaymentMode.payUpFront` mode

  * No initial charge, for `SKProductDiscount.PaymentMode.freeTrial` mode.

Use the payment mode to display an accurate description of the product
discount in your UI. For design guidance, see Human Interface Guidelines > In-
App Purchase.

## See Also

### Getting Price and Payment Mode

`var price: NSDecimalNumber`

The discount price of the product in the local currency.

`var priceLocale: Locale`

The locale used to format the discount price of the product.

`enum SKProductDiscount.PaymentMode`

Values representing the payment modes for a product discount.

Instance Property

# numberOfPeriods

An integer that indicates the number of periods the product discount is
available.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var numberOfPeriods: Int { get }

## Discussion

A product discount may be available for one or more periods. The period,
defined in `subscriptionPeriod`, is a set number of days, weeks, months, or
years.

The total length of time that a product discount is available is calculated by
multiplying the `numberOfPeriods` by the period.

Note that the discount period is independent of the product subscription
period.

## See Also

### Getting the Discount Duration

`var subscriptionPeriod: SKProductSubscriptionPeriod`

An object that defines the period for the product discount.

Instance Property

# subscriptionPeriod

An object that defines the period for the product discount.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var subscriptionPeriod: SKProductSubscriptionPeriod { get }

## Discussion

This object represents the duration of a single subscription period. A period
is described as a number of units, where a unit can be a
`SKProduct.PeriodUnit.day`, `SKProduct.PeriodUnit.month`,
`SKProduct.PeriodUnit.week`, or `SKProduct.PeriodUnit.year`.

To calculate the total amount of time that the discount price is available to
the user, multiply the `subscriptionPeriod` by `numberOfPeriods`.

Note

The subscription period for the discount is independent of the product's
regular subscription period, and does not have to match in units or duration.

## See Also

### Getting the Discount Duration

`var numberOfPeriods: Int`

An integer that indicates the number of periods the product discount is
available.

