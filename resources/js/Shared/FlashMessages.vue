<template>
    <div v-if="show">
        <alert
            :show="showSuccess"
            type="success"
            class="mb-1"
            :message="$page.messages.success"
            @close="showSuccess = false"
        />
        <alert
            :show="showError"
            type="error"
            class="mb-1"
            :message="$page.messages.error"
            @close="showError = false"
        />
        <alert
            :show="showDanger"
            type="danger"
            class="mb-1"
            :message="$page.messages.danger"
            @close="showDanger = false"
        />
        <alert
            :show="showWarning"
            type="warning"
            class="mb-1"
            :message="$page.messages.warning"
            @close="showWarning = false"
        />
        <alert
            :show="showInfo"
            type="info"
            class="mb-1"
            :message="$page.messages.info"
            @close="showInfo = false"
        />
    </div>
</template>

<script>
    import Alert from '@/Shared/Alert'

    export default {
        components: { Alert },
        data () {
            return {
                show: false,
                showSuccess: Boolean(this.$page.messages.success),
                showError: Boolean(this.$page.messages.error),
                showDanger: Boolean(this.$page.messages.danger),
                showWarning: Boolean(this.$page.messages.warning),
                showInfo: Boolean(this.$page.messages.info)
            }
        },
        created () {
            this.show = this.showSuccess ||
                this.showError ||
                this.showDanger ||
                this.showWarning ||
                this.showInfo
        }
    }
</script>

<style scoped>

</style>
