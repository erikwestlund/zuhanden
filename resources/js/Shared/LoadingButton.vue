<template>
    <button
        :disabled="loading"
        class="flex justify-center items-center"
    >
        <loading-spinner
            v-if="loading"
            class="mr-2"
        />
        <slot />
    </button>
</template>

<script>
    import LoadingSpinner from '@/Shared/LoadingSpinner'

    export default {
        components: { LoadingSpinner },
        props: {
            loading: Boolean
        }
    }
</script>
