Initializer

# init(from:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(from decoder: any Decoder) throws

## Relationships

### From Protocol

  * `Decodable`

Instance Method

# format(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func format(_ value: Product.SubscriptionPeriod.Unit) -> String

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

`func encode(to: any Encoder)`

Instance Method

# locale(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func locale(_ locale: Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func encode(to: any Encoder)`

Instance Method

# encode(to:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func encode(to encoder: any Encoder) throws

## Relationships

### From Protocol

  * `Encodable`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit.FormatStyle, rhs: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing period unit formats

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (a: Product.SubscriptionPeriod.Unit.FormatStyle, b: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput = Product.SubscriptionPeriod.Unit

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput`

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput = String

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput`

Generic Type Method

# list(type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<Base>(
        type: ListFormatStyle<StringStyle, Base>.ListType,
        width: ListFormatStyle<StringStyle, Base>.Width = .standard
    ) -> ListFormatStyle<StringStyle, Base> where Base : Sequence, Base.Element == String

## See Also

### Applying list styles

`static func list<MemberStyle, Base>(memberStyle: MemberStyle, type:
ListFormatStyle<MemberStyle, Base>.ListType, width:
ListFormatStyle<MemberStyle, Base>.Width) -> ListFormatStyle<MemberStyle,
Base>`

Generic Type Method

# list(memberStyle:type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<MemberStyle, Base>(
        memberStyle: MemberStyle,
        type: ListFormatStyle<MemberStyle, Base>.ListType,
        width: ListFormatStyle<MemberStyle, Base>.Width = .standard
    ) -> ListFormatStyle<MemberStyle, Base> where MemberStyle : FormatStyle, Base : Sequence, MemberStyle.FormatInput == Base.Element, MemberStyle.FormatOutput == String

## See Also

### Applying list styles

`static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType,
width: ListFormatStyle<StringStyle, Base>.Width) ->
ListFormatStyle<StringStyle, Base>`

Generic Type Method

# measurement(width:usage:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement<UnitType>(
        width: Measurement<UnitType>.FormatStyle.UnitWidth,
        usage: MeasurementFormatUnitUsage<UnitType> = .general,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitType>.FormatStyle where UnitType : Dimension

## See Also

### Applying measurement styles

`static func measurement(width:
Measurement<UnitTemperature>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitTemperature>, hidesScaleName: Bool,
numberFormatStyle: FloatingPointFormatStyle<Double>?) ->
Measurement<UnitTemperature>.FormatStyle`

Type Method

# measurement(width:usage:hidesScaleName:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement(
        width: Measurement<UnitTemperature>.FormatStyle.UnitWidth = .abbreviated,
        usage: MeasurementFormatUnitUsage<UnitTemperature> = .general,
        hidesScaleName: Bool = false,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitTemperature>.FormatStyle

## See Also

### Applying measurement styles

`static func measurement<UnitType>(width:
Measurement<UnitType>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitType>, numberFormatStyle:
FloatingPointFormatStyle<Double>?) -> Measurement<UnitType>.FormatStyle`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<Value>(code: String) -> FloatingPointFormatStyle<Value>.Currency where Value : BinaryFloatingPoint

## See Also

### Applying currency styles

`static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency where V : BinaryInteger

## See Also

### Applying currency styles

`static func currency<Value>(code: String) ->
FloatingPointFormatStyle<Value>.Currency`

Initializer

# init(from:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(from decoder: any Decoder) throws

## Relationships

### From Protocol

  * `Decodable`

Instance Method

# format(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func format(_ value: Product.SubscriptionPeriod.Unit) -> String

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

`func encode(to: any Encoder)`

Instance Method

# locale(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func locale(_ locale: Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func encode(to: any Encoder)`

Instance Method

# encode(to:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func encode(to encoder: any Encoder) throws

## Relationships

### From Protocol

  * `Encodable`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit.FormatStyle, rhs: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing period unit formats

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (a: Product.SubscriptionPeriod.Unit.FormatStyle, b: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput = Product.SubscriptionPeriod.Unit

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput`

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput = String

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput`

Generic Type Method

# list(type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<Base>(
        type: ListFormatStyle<StringStyle, Base>.ListType,
        width: ListFormatStyle<StringStyle, Base>.Width = .standard
    ) -> ListFormatStyle<StringStyle, Base> where Base : Sequence, Base.Element == String

## See Also

### Applying list styles

`static func list<MemberStyle, Base>(memberStyle: MemberStyle, type:
ListFormatStyle<MemberStyle, Base>.ListType, width:
ListFormatStyle<MemberStyle, Base>.Width) -> ListFormatStyle<MemberStyle,
Base>`

Generic Type Method

# list(memberStyle:type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<MemberStyle, Base>(
        memberStyle: MemberStyle,
        type: ListFormatStyle<MemberStyle, Base>.ListType,
        width: ListFormatStyle<MemberStyle, Base>.Width = .standard
    ) -> ListFormatStyle<MemberStyle, Base> where MemberStyle : FormatStyle, Base : Sequence, MemberStyle.FormatInput == Base.Element, MemberStyle.FormatOutput == String

## See Also

### Applying list styles

`static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType,
width: ListFormatStyle<StringStyle, Base>.Width) ->
ListFormatStyle<StringStyle, Base>`

Generic Type Method

# measurement(width:usage:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement<UnitType>(
        width: Measurement<UnitType>.FormatStyle.UnitWidth,
        usage: MeasurementFormatUnitUsage<UnitType> = .general,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitType>.FormatStyle where UnitType : Dimension

## See Also

### Applying measurement styles

`static func measurement(width:
Measurement<UnitTemperature>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitTemperature>, hidesScaleName: Bool,
numberFormatStyle: FloatingPointFormatStyle<Double>?) ->
Measurement<UnitTemperature>.FormatStyle`

Type Method

# measurement(width:usage:hidesScaleName:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement(
        width: Measurement<UnitTemperature>.FormatStyle.UnitWidth = .abbreviated,
        usage: MeasurementFormatUnitUsage<UnitTemperature> = .general,
        hidesScaleName: Bool = false,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitTemperature>.FormatStyle

## See Also

### Applying measurement styles

`static func measurement<UnitType>(width:
Measurement<UnitType>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitType>, numberFormatStyle:
FloatingPointFormatStyle<Double>?) -> Measurement<UnitType>.FormatStyle`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<Value>(code: String) -> FloatingPointFormatStyle<Value>.Currency where Value : BinaryFloatingPoint

## See Also

### Applying currency styles

`static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency where V : BinaryInteger

## See Also

### Applying currency styles

`static func currency<Value>(code: String) ->
FloatingPointFormatStyle<Value>.Currency`

Initializer

# init(from:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    init(from decoder: any Decoder) throws

## Relationships

### From Protocol

  * `Decodable`

Instance Method

# format(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func format(_ value: Product.SubscriptionPeriod.Unit) -> String

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

`func encode(to: any Encoder)`

Instance Method

# locale(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func locale(_ locale: Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle

## Relationships

### From Protocol

  * `FormatStyle`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func encode(to: any Encoder)`

Instance Method

# encode(to:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func encode(to encoder: any Encoder) throws

## Relationships

### From Protocol

  * `Encodable`

## See Also

### Formatting subscription period units

`func format(Product.SubscriptionPeriod.Unit) -> String`

`func locale(Locale) -> Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit.FormatStyle, rhs: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing period unit formats

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (a: Product.SubscriptionPeriod.Unit.FormatStyle, b: Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing period unit formats

`static func != (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit.FormatStyle,
Product.SubscriptionPeriod.Unit.FormatStyle) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput = Product.SubscriptionPeriod.Unit

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput`

Type Alias

# Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatOutput = String

## See Also

### Getting data types

`typealias Product.SubscriptionPeriod.Unit.FormatStyle.FormatInput`

Generic Type Method

# list(type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<Base>(
        type: ListFormatStyle<StringStyle, Base>.ListType,
        width: ListFormatStyle<StringStyle, Base>.Width = .standard
    ) -> ListFormatStyle<StringStyle, Base> where Base : Sequence, Base.Element == String

## See Also

### Applying list styles

`static func list<MemberStyle, Base>(memberStyle: MemberStyle, type:
ListFormatStyle<MemberStyle, Base>.ListType, width:
ListFormatStyle<MemberStyle, Base>.Width) -> ListFormatStyle<MemberStyle,
Base>`

Generic Type Method

# list(memberStyle:type:width:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func list<MemberStyle, Base>(
        memberStyle: MemberStyle,
        type: ListFormatStyle<MemberStyle, Base>.ListType,
        width: ListFormatStyle<MemberStyle, Base>.Width = .standard
    ) -> ListFormatStyle<MemberStyle, Base> where MemberStyle : FormatStyle, Base : Sequence, MemberStyle.FormatInput == Base.Element, MemberStyle.FormatOutput == String

## See Also

### Applying list styles

`static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType,
width: ListFormatStyle<StringStyle, Base>.Width) ->
ListFormatStyle<StringStyle, Base>`

Generic Type Method

# measurement(width:usage:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement<UnitType>(
        width: Measurement<UnitType>.FormatStyle.UnitWidth,
        usage: MeasurementFormatUnitUsage<UnitType> = .general,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitType>.FormatStyle where UnitType : Dimension

## See Also

### Applying measurement styles

`static func measurement(width:
Measurement<UnitTemperature>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitTemperature>, hidesScaleName: Bool,
numberFormatStyle: FloatingPointFormatStyle<Double>?) ->
Measurement<UnitTemperature>.FormatStyle`

Type Method

# measurement(width:usage:hidesScaleName:numberFormatStyle:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func measurement(
        width: Measurement<UnitTemperature>.FormatStyle.UnitWidth = .abbreviated,
        usage: MeasurementFormatUnitUsage<UnitTemperature> = .general,
        hidesScaleName: Bool = false,
        numberFormatStyle: FloatingPointFormatStyle<Double>? = nil
    ) -> Measurement<UnitTemperature>.FormatStyle

## See Also

### Applying measurement styles

`static func measurement<UnitType>(width:
Measurement<UnitType>.FormatStyle.UnitWidth, usage:
MeasurementFormatUnitUsage<UnitType>, numberFormatStyle:
FloatingPointFormatStyle<Double>?) -> Measurement<UnitType>.FormatStyle`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<Value>(code: String) -> FloatingPointFormatStyle<Value>.Currency where Value : BinaryFloatingPoint

## See Also

### Applying currency styles

`static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency`

Generic Type Method

# currency(code:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currency<V>(code: String) -> IntegerFormatStyle<V>.Currency where V : BinaryInteger

## See Also

### Applying currency styles

`static func currency<Value>(code: String) ->
FloatingPointFormatStyle<Value>.Currency`

