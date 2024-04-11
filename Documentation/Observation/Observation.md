# Hashable Implementations

Instance Property

# hashValue

The hash value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var hashValue: Int { get }

## Discussion

Hash values are not guaranteed to be equal across different executions of your
program. Do not save hash values to use during a future execution.

Important

`hashValue` is deprecated as a `Hashable` requirement. To conform to
`Hashable`, implement the `hash(into:)` requirement instead. The compiler
provides an implementation for `hashValue` for you.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Discussion

Implement this method to conform to the `Hashable` protocol. The components
used for hashing must be the same as the components compared in your type’s
`==` operator implementation. Call `hasher.combine(_:)` with each of these
components.

Important

In your implementation of `hash(into:)`, don’t call `finalize()` on the
`hasher` instance provided, or replace it with a different instance. Doing so
may become a compile-time error in the future.



# Decodable Implementations

Initializer

# init(from:)

Creates a new instance by decoding from the given decoder.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(from decoder: any Decoder) throws

##  Parameters

`decoder`

    

The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the
data read is corrupted or otherwise invalid.



# ObservationRegistrar

Initializer

# init()

Creates an instance of the observation registrar.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()

## Discussion

You don’t need to create an instance of `ObservationRegistrar` when using the
`Observable()` macro to indicate observably of a type.

Instance Method

# willSet(_:keyPath:)

A property observation called before setting the value of the subject.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func willSet<Subject, Member>(
        _ subject: Subject,
        keyPath: KeyPath<Subject, Member>
    ) where Subject : Observable

##  Parameters

`subject`

    

An instance of an observable type.

`keyPath`

    

The key path of an observed property.

## See Also

### Receiving change notifications

`func didSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)`

A property observation called after setting the value of the subject.

Instance Method

# didSet(_:keyPath:)

A property observation called after setting the value of the subject.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func didSet<Subject, Member>(
        _ subject: Subject,
        keyPath: KeyPath<Subject, Member>
    ) where Subject : Observable

##  Parameters

`subject`

    

An instance of an observable type.

`keyPath`

    

The key path of an observed property.

## See Also

### Receiving change notifications

`func willSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)`

A property observation called before setting the value of the subject.

Instance Method

# access(_:keyPath:)

Registers access to a specific property for observation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func access<Subject, Member>(
        _ subject: Subject,
        keyPath: KeyPath<Subject, Member>
    ) where Subject : Observable

##  Parameters

`subject`

    

An instance of an observable type.

`keyPath`

    

The key path of an observed property.

## See Also

### Identifying transactional access

`func withMutation<Subject, Member, T>(of: Subject, keyPath: KeyPath<Subject,
Member>, () throws -> T) rethrows -> T`

Identifies mutations to the transactions registered for observers.

Instance Method

# withMutation(of:keyPath:_:)

Identifies mutations to the transactions registered for observers.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func withMutation<Subject, Member, T>(
        of subject: Subject,
        keyPath: KeyPath<Subject, Member>,
        _ mutation: () throws -> T
    ) rethrows -> T where Subject : Observable

##  Parameters

`of`

    

An instance of an observable type.

`keyPath`

    

The key path of an observed property.

## Discussion

This method calls `willSet(_:keyPath:)` before the mutation. Then it calls
`didSet(_:keyPath:)` after the mutation.

## See Also

### Identifying transactional access

`func access<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)`

Registers access to a specific property for observation.



# Encodable Implementations

Instance Method

# encode(to:)

Encodes this value into the given encoder.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func encode(to encoder: any Encoder)

##  Parameters

`encoder`

    

The encoder to write data to.

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed
container in its place.

This function throws an error if any values are invalid for the given
encoder’s format.



# Equatable Implementations

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

Observation  Swift  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static func != (lhs: Self, rhs: Self) -> Bool

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

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func == (lhs: ObservationRegistrar, rhs: ObservationRegistrar) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b`
implies that `a != b` is `false`.



