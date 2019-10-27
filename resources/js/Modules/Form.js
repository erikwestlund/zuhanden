import Errors from './Errors.js'

export default class Form {
    /**
     * Create a new Form instance.
     *
     * @param {object} data
     */
    constructor (data, isUpdateForm = false, dontReset = false) {
        this.originalData = _.cloneDeep(data)
        this.dontReset = dontReset

        for (const field in data) {
            this[field] = data[field]
        }

        this.formType = isUpdateForm ? 'update' : 'create'
        this.errors = new Errors()
    }

    /**
     * Fetch all relevant data for the form.
     */
    data () {
        const data = {}

        for (const property in this.originalData) {
            data[property] = this[property]
        }

        return data
    }

    /**
     * Reset the form fields.
     */
    reset (force_reset = false) {
        if (this.formType === 'create') {
            for (const field in this.originalData) {
                this[field] = this.originalData[field]
            }
        }

        this.errors.clear()
    }

    /**
     * Send a POST request to the given URL.
     * .
     * @param {string} url
     */
    post (url) {
        return this.submit('post', url)
    }

    /**
     * Send a PUT request to the given URL.
     * .
     * @param {string} url
     */
    put (url) {
        return this.submit('put', url)
    }

    /**
     * Send a PATCH request to the given URL.
     * .
     * @param {string} url
     */
    patch (url) {
        return this.submit('patch', url)
    }

    /**
     * Send a DELETE request to the given URL.
     * .
     * @param {string} url
     */
    delete (url) {
        return this.submit('delete', url)
    }

    /**
     * Submit the form.
     *
     * @param {string} requestType
     * @param {string} url
     */
    submit (requestType, url) {
        return new Promise((resolve, reject) => {
            axios[requestType](url, this.data())
                .then((response) => {
                    if (!this.dontReset) {
                        this.onSuccess(response.data)
                    }

                    resolve(response.data)
                })
                .catch((error) => {
                    this.onFail(error.response.data)
                    reject(error.response)
                })
        })
    }

    /**
     * Handle a successful form submission.
     *
     * @param {object} data
     */
    onSuccess (data) {
        this.reset()
    }

    /**
     * Handle a failed form submission.
     *
     * Only record if an error bag is returned. This allows us to defer
     * to the caller to handle things like authorization errors.
     *
     * @param {object} errors
     */
    onFail (errors) {
        if (errors.hasOwnProperty('errors')) {
            this.errors.record(errors.errors)
        }
    }
}
