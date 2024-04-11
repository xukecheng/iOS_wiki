Instance Property

# id

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var id: Value.ID { get }

Available when `Value` conforms to `Identifiable`.

## See Also

### Managing changes

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

