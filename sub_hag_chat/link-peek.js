class LinkPeek extends HTMLElement {
  static register(tagName) {
    if ("customElements" in window) {
      customElements.define(tagName || "link-peek", LinkPeek);
    }
  }

  static get observedAttributes() {
    return ['api'];
  }

  async attributeChangedCallback(attrName, oldVal, newVal) {
    console.log("Attribute changed")
    if (attrName === "api") {
      //this.append(this.template);

      const data = { ...(await this.data), link: this.link };

      this.slots.forEach((slot) => {
        slot.dataset.key.split(",").forEach((keyItem) => {
          const value = this.getValue(keyItem, data);
          this.populateSlot(slot, value);
        });
      });
    }
  }

  async connectedCallback() {
    console.log("Connected")
    this.append(this.template);

    const data = { ...(await this.data), link: this.link };

    this.slots.forEach((slot) => {
      slot.dataset.key.split(",").forEach((keyItem) => {
        const value = this.getValue(keyItem, data);
        this.populateSlot(slot, value);
      });
    });
  }

  populateSlot(slot, value) {
    if (slot.localName === "a") { 
      if (typeof value == "string" && value.startsWith("http")) {
        slot.href = value;
      } else {
        slot.textContent = value;
      }
    } else if (slot.localName === "img") {
      slot.src = value;
    }  else {
      slot.textContent = value;
    }
  }

  handleKey(object, key) {
    if (object !=null) {
      const parsedKeyInt = parseFloat(key);

      if (Number.isNaN(parsedKeyInt)) {
        return object[key];
      }

      return object[parsedKeyInt];
    } // if this is the image url, replace with another image?
    return "./placeholder.png"
  }

  getValue(string, data) {
    let keys = string.trim().split(/\.|\[|\]/g);
    keys = keys.filter((string) => string.length);

    const value = keys.reduce(
      (object, key) => this.handleKey(object, key),
      data
    );
    return value;
  }

  get template() {
    return document
      .getElementById(
        this.getAttribute("template") || `${this.localName}-template`
      )
      .content.cloneNode(true);
  }

  get slots() {
    return this.querySelectorAll("[data-key]");
  }

  get link() {
    return this.querySelector("#random-link").href;
  }

  get endpoint() {
    return this.getAttribute("api").replace("${link}", this.link);
  }

  get data() {
    return fetch(this.endpoint).then((response) => response.json());
  }
}

LinkPeek.register();
