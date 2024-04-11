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

