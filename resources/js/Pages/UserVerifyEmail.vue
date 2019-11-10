<template>
    <layout :title="title">
        <h1 class="text-2xl">
            {{ title }}
        </h1>
        <p class="mt-8">
            {{ message }}
        </p>
    </layout>
</template>

<script>
    import Layout from '@/Shared/Layout'

    export default {
        components: {
            Layout
        },
        props: {
            success: Boolean
        },
        computed: {
            title () {
                return this.success ? 'Email Verification Successful' : 'Email Verification Failed'
            },
            message () {
                return this.success
                    ? 'Your email has been verified.'
                    : 'We could not verify your email.'
            }
        }
    }
</script>

<style scoped>

</style>
