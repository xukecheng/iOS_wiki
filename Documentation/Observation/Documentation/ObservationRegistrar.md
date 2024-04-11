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

