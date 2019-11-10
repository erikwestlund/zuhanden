<template>
    <span>
        <fa-icon
            class="mr-2 fa-spin"
            :icon="['far', 'circle-notch']"
        />
        {{ submittingText }}
    </span>
</template>

<script>
    export default {
        props: {
            submitting: {
                type: Boolean,
                default: false
            },
            type: {
                type: String,
                default: 'submitting'
            }
        },

        computed: {
            submittingText () {
                if (this.type === 'saving') {
                    return 'Saving...'
                } else if (this.type === 'deleting') {
                    return 'Deleting...'
                } else if (this.type === 'logging_in') {
                    return 'Logging in...'
                } else if (this.type === 'publishing') {
                    return 'Publishing...'
                } else if (this.type === 'sending') {
                    return 'Sending...'
                } else if (this.type === 'unpublishing') {
                    return 'Unpublishing...'
                } else if (this.type === 'uploading') {
                    return 'Uploading...'
                } else if (this.type === 'uploading_image') {
                    return 'Uploading Image...'
                } else {
                    return 'Submitting...'
                }
            }
        }
    }
</script>
